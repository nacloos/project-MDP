import numpy as np

# define some constants for the game
START_STATE = 0
JUNCTION_STATE = 2
FINAL_STATE = 14
FAST_LANE_START = 10

SECURITY_DICE = 1
NORMAL_DICE = 2
RISKY_DICE = 3

NO_TRAP = 0
RESTART_TRAP = 1
PENALTY_TRAP = 2
PRISON_TRAP = 3
GAMBLE_TRAP = 4


class SnakesAndLaddersProb:
    """
    Probability transitions of the Snakes and Ladders game.
    """
    def __init__(self, layout, circle):
        self.layout = layout
        self.circle = circle

        # self.action_space = [SECURITY_DICE]
        self.action_space = [SECURITY_DICE, NORMAL_DICE]
        # self.action_space = [SECURITY_DICE, NORMAL_DICE, RISKY_DICE]
        
        self.n_states = len(layout)
        self.R = -np.ones(self.n_states) # reward of -1 for each state excepted the last one
        self.R[-1] = 0


    def p(self, s, a):
        if a == SECURITY_DICE:
            P = self.move(s, 1)
            return P, self.R[s]

        elif a == NORMAL_DICE:
            P = self.move(s, 2)
            P_trap, r_trap = self.traps(P.copy()) # transition prob if would always trigger traps
            P = P/2 + P_trap/2
            r = self.R[s]/2 + r_trap/2 # TODO return the expected reward ?
            return P, r

        elif a == RISKY_DICE:
            P = self.move(s, 3)
            P, r = self.traps(P)
            return P, r

        else:
            print("Invalid action")


    def move(self, s, max_steps):
        def dist_from_final(s):
            if s >= FINAL_STATE:
                return 0
            elif s >= FAST_LANE_START: 
                # on the fast lane
                return FINAL_STATE-s
            elif s > JUNCTION_STATE and s < FAST_LANE_START:
                # on the slow lane 
                return FINAL_STATE-s-4
            else: 
                return 7-s  

        P = np.zeros(self.n_states)

        if s != JUNCTION_STATE:
            for i in range(max_steps+1):
                if dist_from_final(s)-i > 0:
                    # just move forward
                    P[s+i] = 1/(max_steps+1)
                elif not self.circle or s+i == FINAL_STATE:
                    # don't circle or if circle, stop on the final state
                    P[FINAL_STATE] += 1/(max_steps+1)
                else:
                    # circle and go over the final state
                    # P[i-dist_from_final(s)-1] = 1/(max_steps+1) # come back at the beginning
                    P[START_STATE] = 1/(max_steps+1) # come back at the beginning

        else:
            P[JUNCTION_STATE] = 1/(max_steps+1) # don't move
            for i in range(1,max_steps+1):
                P[JUNCTION_STATE+i] = 1/2*1/(max_steps+1) # move into the slow lane
                P[FAST_LANE_START+i-1] = 1/2*1/(max_steps+1) # move into the fast lane

        return P


    def traps(self, P):
        next_states = np.argwhere(P != 0).reshape(-1) # all the possible next states
        r = -1 # mean reward

        for next_s in next_states:
            if next_s == FINAL_STATE or next_s == START_STATE:
                continue

            if self.layout[next_s] == RESTART_TRAP:
                if next_s > 0:
                    P[0] += P[next_s]
                    P[next_s] = 0

            elif self.layout[next_s] == PENALTY_TRAP:
                if next_s >= 3:
                    # check if don't cross the junction
                    if next_s >= FAST_LANE_START and next_s-3 < FAST_LANE_START:
                        P[next_s-10] += P[next_s]
                    else:
                        P[next_s-3] += P[next_s]
                    P[next_s] = 0
                else:
                    p_temp = P[next_s]
                    P[next_s] = 0
                    P[0] += p_temp


            elif self.layout[next_s] == PRISON_TRAP:
                r = (1-P[next_s])*(-1) + P[next_s]*(-2)

            elif self.layout[next_s] == GAMBLE_TRAP:
                p_temp = P[next_s]
                P[next_s] = 0
                P += p_temp*1/self.n_states # In-place modification of P !

        return P, r


# def p_security(s, circle):
    """
    Transition probabilty p(s'|s,a), assuming the security dice.
    """
    # P = np.zeros(n_states)
    # if s == JUNCTION_STATE:
    #     P[s] = 1/2
    #     P[s+1] = 1/4
    #     P[FAST_LANE_START] = 1/4
    # else:
    #     P[s] = 1/2
    #     P[s+1] = 1/2

    # return P, R[s]





if __name__ == '__main__':
    game = SnakesAndLaddersSim([], False)
    game.reset()
    game.step(SECURITY_DICE)