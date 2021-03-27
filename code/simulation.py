from snakes_and_ladders_sim import SnakesAndLaddersSim, SECURITY_DICE, NORMAL_DICE, RISKY_DICE
from agent import ConstantAgent
import numpy as np



def estimate_cost(layout, circle, agent, n_episodes=int(1e4)):
    # first-visit monte carlo
    env = SnakesAndLaddersSim(layout, circle)

    V = np.zeros(15)

    for episode in range(1,n_episodes+1):
        visited = np.zeros(15, dtype=np.bool) # true if state already visited in the current episode 
        cum_reward = np.zeros(15) # sum of rewards, starting at state first visit

        state = env.reset()
        visited[state] = True

        done = False
        while not done:
            action = agent.select_action(state)
            next_state, reward, done = env.step(action)

            cum_reward[visited] += reward       
            if next_state <= 14 and not visited[next_state]:
                visited[next_state] = True

            state = next_state                
        
        V[visited] += 1/episode*(cum_reward[visited] - V[visited])

    C = -V[:-1]
    return C
    

def estimate_prob(layout, circle, dice, n_episodes=int(5e3)):
    env = SnakesAndLaddersSim(layout, circle)
    agent = ConstantAgent(dice)

    proba = np.zeros((15, 15))
    count = np.zeros((15, 1))

    for episode in range(n_episodes):
        state = env.reset()
        done = False
        while not done:
            action = agent.select_action(state)
            next_state, reward, done = env.step(action)
            if next_state <= 14:
                proba[state, next_state] += 1
            count[state] += 1
            state = next_state                

    proba[:-1] /= count[:-1]
    proba[-1,-1] = 1.0 # state 14 is absorbing
    return proba


if __name__ == '__main__':
    layout = np.zeros(15)
    circle = False
    agent = ConstantAgent(SECURITY_DICE)
    C = estimate_cost(layout, circle, agent)
    print(C)
