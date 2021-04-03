from snakes_and_ladders_sim import SnakesAndLaddersSim, SECURITY_DICE, NORMAL_DICE, RISKY_DICE
from agent import ConstantAgent
import numpy as np


def estimate_cost(layout, circle, agent, n_episodes=int(1e3), save_steps=None):
    # first-visit monte carlo
    env = SnakesAndLaddersSim(layout, circle, random_start=True)

    V = np.zeros(15)
    counts = np.zeros(15)
    if save_steps is not None:
        C_save = np.zeros((n_episodes//save_steps+1, 14))
    # returns = np.zeros((n_episodes, 15))

    for episode in range(1,n_episodes+1):
        visited = np.zeros(15, dtype=np.bool) # true if state already visited in the current episode 
        G = np.zeros(15) # sum of rewards, starting at state first visit

        state = env.reset()
        visited[state] = True

        done = False
        while not done:
            action = agent.select_action(state)
            next_state, reward, done = env.step(action)

            G[visited] += reward       
            if next_state <= 14 and not visited[next_state]:
                visited[next_state] = True

            state = next_state              
        V[visited] = V[visited] + 1/(counts[visited]+1)*(G[visited] - V[visited])
        # returns[episode-1] = G
        counts[visited] += 1  
        
        if save_steps is not None and episode % save_steps == 0:
            C_save[episode//save_steps] = -V[:-1]


    # V_est = np.sum(returns, axis=0) / counts
    # print(np.allclose(V, V_est))
    C = -V[:-1]
    if save_steps is not None:
        return C, C_save
    else:
        return C



# def estimate_cost_TD(layout, circle, agent, n_episodes=int(1e4)):
#     # TD-learning
#     env = SnakesAndLaddersSim(layout, circle)

#     V = np.zeros(15)
#     n_updates = np.ones(15)

#     for episode in range(1,n_episodes+1):
#         state = env.reset()
#         done = False
#         while not done:
#             action = agent.select_action(state)
#             next_state, reward, done = env.step(action)

#             V[state] += 1/n_updates[state]*(reward + V[next_state] - V[state])
#             n_updates[state] += 1

#             state = next_state                

#     C = -V[:-1]
#     return C
    

def estimate_prob(layout, circle, dice, n_episodes=int(5e3)):
    env = SnakesAndLaddersSim(layout, circle, random_start=True)
    agent = ConstantAgent(dice)

    proba = np.zeros((15, 15))
    count = np.zeros((15, 1))

    for episode in range(n_episodes):
        state = env.reset()
        done = False
        while not done:
            action = agent.select_action(state)
            next_state, reward, done = env.step(action)
            
            proba[state, next_state] += 1
            count[state] += 1
            state = next_state                

    # visited = np.argwhere(count[:-1] != 0)
    proba[:-1] /= count[:-1]
    proba[-1,-1] = 1.0 # state 14 is absorbing
    return proba


if __name__ == '__main__':
    layout = np.zeros(15)
    circle = False
    agent = ConstantAgent(SECURITY_DICE)
    C = estimate_cost(layout, circle, agent)
    print(C)
