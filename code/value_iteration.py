import numpy as np

from snakes_and_ladders import SnakesAndLaddersProb


def markovDecision(layout, circle, actions=None, tol=1e-9):
    """
        actions: set of possible actions, 
        e.g. if actions = [NORMAL_DICE] compute the value of a constant normal dice policy,
        if actions = None, compute the optimal value function considering the three dices.
    """
    # create a game environment
    env = SnakesAndLaddersProb(layout, circle)
    if not actions:
        actions = env.action_space # consider the three dices
    n_states = len(layout)
    V = np.zeros(n_states)

    # value iteration
    while True:
        new_V = np.zeros(n_states)

        for s in range(n_states-1):
            Q = np.zeros(len(actions)) # value of state s and action a
            for i, a in enumerate(actions):
                P, r = env.p(s, a) # transition probabilities and reward
                Q[i] = np.dot(P, r + V) # E[R + V(s')|s,a]

            new_V[s] = np.max(Q)
            
        if np.max(np.abs(new_V-V)) > tol:
            V = new_V
        else:
            break

    # compute the optimal policy
    opt_policy = np.zeros(n_states-1)
    for s in range(n_states-1):
        Q = np.zeros(len(actions))
        for i, a in enumerate(actions):
            P, r = env.p(s, a)
            Q[i] = np.dot(P, r + V)

        opt_policy[s] = np.argmax(Q)+1

    expec = -V[:-1] # expected cost, excluding the final state
    return expec, opt_policy



if __name__ == '__main__':
    layout = np.zeros(15)
    layout[9] = 1
    circle = False 
    C, pi = markovDecision(layout, circle)
    print(C[:10], C[10:])
    print(pi[:10], pi[10:])

