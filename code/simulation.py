from snakes_and_ladders import SnakesAndLaddersSim, SECURITY_DICE, NORMAL_DICE, RISKY_DICE
from agent import ConstantAgent


def simulate(layout, circle):
    env = SnakesAndLaddersSim(layout, circle)
    agent = ConstantAgent(SECURITY_DICE)

    n_episodes = 50

    for episode in range(n_episodes):
        state = env.reset()
        done = False
        while not done:
            action = agent.select_action(state)
            next_state, reward, done = env.step(action)

            agent.update(state, action, reward, next_state)


if __name__ == '__main__':
    simulate([], [])