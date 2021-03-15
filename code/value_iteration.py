import numpy as np


JUNCTION_STATE = 2
FINAL_STATE = 14
FAST_LANE_START = 10
n_states = 15

SECURITY_DICE = 1
NORMAL_DICE = 2
RISKY_DICE = 3
actions = [SECURITY_DICE, NORMAL_DICE, RISKY_DICE]

NO_TRAP = 0
RESTART_TRAP = 1
PENALTY_TRAP = 2
PRISON_TRAP = 3
GAMBLE_TRAP = 4

R = -np.ones(n_states) # reward of -1 for each state expected the last one
R[-1] = 0


def p(s, a):
    if a == SECURITY_DICE:
        return p_security(s)
    elif a == NORMAL_DICE:
        return p_normal(s)
    elif a == RISKY_DICE:
        return p_risky(s)
    else:
        print("Invalid action")


def p_security(s):
    """
    Transition probabilty p(s'|s), assuming the security dice.
    """
    P = np.zeros(n_states)
    if s == JUNCTION_STATE:
        P[s] = 1/2
        P[s+1] = 1/4
        P[FAST_LANE_START] = 1/4
    else:
        P[s] = 1/2
        P[s+1] = 1/2

    return P, R[s]


def p_normal(s):
    P = np.zeros(n_states)
    return P, R[s]


def p_risky(s):
    P = np.zeros(n_states)
    return P, R[s]


def markovDecision(tol=1e-9):
    V = np.zeros(n_states)

    while True:
        new_V = np.zeros(n_states)

        for s in range(n_states-1):
            Q = np.zeros(3) # value of state s and action a
            for i, a in enumerate(actions):
                P, r = p(s,a) # transition probabilities and reward
                Q[i] = np.dot(P, r + V) # E[R + V(s')|s,a]

            # new_V = np.max(Q)
            new_V[s] = Q[0] # only the security dice 
            
        if np.max(np.abs(new_V-V)) > tol:
            V = new_V
        else:
            break

    expec = -V[:-1] # expected cost, excluding the final state
    return expec

C = markovDecision()
print(C)




# def move(s, a):
#     P = np.zeros(n_states)
#     if a == SECURITY_DICE:
#         P[s] = 1/2
#         P[s+1] = 1/2
#     else if a == NORMAL_DICE:
#         P[s] = 1/3
#         P[s+1] = 1/3
#         P[s+2] = 1/3
#     else if a == RISKY_DICE:
#         P[s] = 1/4
#         P[s+1] = 1/4
#         P[s+2] = 1/4
#         P[s+3] = 1/4
