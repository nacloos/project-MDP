from snakes_and_ladders_sim import SnakesAndLaddersSim, SECURITY_DICE, NORMAL_DICE, RISKY_DICE
from agent import ConstantAgent
import numpy as np


def simulate(layout, circle):
    env = SnakesAndLaddersSim(layout, circle)
    # agent = ConstantAgent(SECURITY_DICE)
    agent = ConstantAgent(NORMAL_DICE)

    n_episodes = 50000
    proba = np.zeros((15, 15))
    count = np.zeros((15, 1))
    tot_reward = np.zeros((15))

    for episode in range(n_episodes):
        state = env.reset()
        done = False
        while not done:
            action = agent.select_action(state)
            next_state, reward, done = env.step(action)
            if next_state <= len(proba)-1:
                # print(state, next_state)
                proba[state, next_state] += 1
                count[state] += 1
            state = next_state
            # agent.update(state, action, reward, next_state)

    proba /= count
    # proba = np.nan_to_num(proba)
    print(proba)
    print(proba[2, 10])
    print(proba[2, 2])


if __name__ == '__main__':
    layout = np.zeros(15)
    simulate(layout, False)