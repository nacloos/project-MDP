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


class SnakesAndLaddersSim:
    """
    Simulation of the Snakes and Ladders game.
    """
    def __init__(self, layout, circle):
        """
        Create a Snakes and Ladders game
        :param layout: layout of the game (see project instructions)
        :param circle: boolean, true if the player must land exactly on the final square to win
        """
        self.layout = layout
        self.circle = circle
        self.state_space = list(range(1, 16)) # the squares of the game
        self.action_space = [SECURITY_DICE, NORMAL_DICE, RISKY_DICE]
        self.current_state = START_STATE
        self.reward = 0
        self.tot_reward = 0

    def reset(self):
        """
        Restart the game
        """
        self.current_state = START_STATE
        return START_STATE

    def movement(self, squares):
        # junction
        if self.current_state == JUNCTION_STATE:
            if squares != 0:
                roll = np.random.randint(2)
                if roll == 0:
                    self.current_state = FAST_LANE_START + squares - 1
                else:
                    self.current_state += squares    
        else:
            next_state = self.current_state + squares
            if self.circle & next_state > FINAL_STATE:
                pass
            else:
                self.current_state = next_state

    def trap(self):
        if self.layout[self.current_state] == RESTART_TRAP:
            self.current_state = START_STATE
        elif self.layout[self.current_state] == PENALTY_TRAP:
            if self.current_state in [9, 10, 11]:
                self.current_state -= 9
            self.current_state -= 3
        elif self.layout[self.current_state] == PRISON_TRAP:
            self.reward -= 1
        elif self.layout[self.current_state] == GAMBLE_TRAP:
            self.current_state = np.random.randint(15)

    def step(self, action):
        """
        Perform one action in the environment
        :param action: action taken by the agent
        :return: next state, reward, a boolean which is true when the game is over
        """
        self.reward = -1
        if action == SECURITY_DICE:
            squares = np.random.randint(2)
            trap_chance = 1
        elif action == NORMAL_DICE:
            squares = np.random.randint(3)
            trap_chance = np.random.randint(2)
        elif action ==  RISKY_DICE:
            squares = np.random.randint(4)
            trap_chance = 0

        self.movement(squares)  
        if (trap_chance == 0) & (self.current_state <= FINAL_STATE):
            self.trap()
        done = self.current_state >= FINAL_STATE

        return self.current_state, self.reward, done

# if __name__ == '__main__':
#     layout = np.zeros(15)
#     nb_simulation = 10000
#     print("Initialization of the game\n")
#     game = SnakesAndLaddersSim(layout, False)
#     game.reset()
#     print("Starting state:", START_STATE,"\n")
#     game.game(nb_simulation)



# def game(self, nb_simulation = 100000):
#     proba = np.zeros((15, 15))
#     count = np.zeros((15, 1))
#     tot_reward = np.zeros((15))
#     for i in range(nb_simulation):
#         while self.current_state != FINAL_STATE:
#             previous_state = self.current_state
#             current_state, reward, done = self.step(SECURITY_DICE)
#             # tot_reward[i] += self.reward
#             proba[previous_state, self.current_state] += 1
#             count[previous_state] += 1
#             # count += 1
#             # print("Current state:", self.current_state)
#         self.reset()
#     proba /= count
#     print(proba)
#     print(proba[2, 10])
#     print(proba[2, 2])