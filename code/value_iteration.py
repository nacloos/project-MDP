import numpy as np

from snakes_and_ladders import SnakesAndLaddersProb


def markovDecision(layout, circle, tol=1e-9):
    env = SnakesAndLaddersProb(layout, circle)
    n_states = len(layout)
    V = np.zeros(n_states)

    while True:
        new_V = np.zeros(n_states)

        for s in range(n_states-1):
            Q = np.zeros(3) # value of state s and action a
            for i, a in enumerate(env.action_space):
                P, r = env.p(s, a) # transition probabilities and reward
                Q[i] = np.dot(P, r + V) # E[R + V(s')|s,a]

            # new_V = np.max(Q)
            new_V[s] = Q[0] # only the security dice 
            
        if np.max(np.abs(new_V-V)) > tol:
            V = new_V
        else:
            break

    expec = -V[:-1] # expected cost, excluding the final state
    return expec


if __name__ == '__main__':
    layout = np.zeros(15)
    C = markovDecision(layout, False)
    print(C)
