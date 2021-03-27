import numpy as np
import matplotlib.pyplot as plt

from snakes_and_ladders import SECURITY_DICE, NORMAL_DICE, RISKY_DICE
from value_iteration import markovDecision
import agent
from simulation import estimate_cost

colors = ["#f4f1de","#e07a5f","#3d405b","#81b29a","#f2cc8f"]

def plot_cost():
    layout = np.zeros(15)
    circle = False

    cst_agent = agent.ConstantAgent(SECURITY_DICE)
    C = estimate_cost(layout, circle, cst_agent)
    states = np.arange(len(C))+1

    plt.figure(figsize=(6, 4), dpi=120)
    ax = plt.gca()
    # plt.bar(states, C, width=0.7, color=(0,0,0,0), edgecolor="#FEC5BB", lw=1.8, label="Security dice")
    plt.bar(states, C, width=0.7, color=(0,0,0,0), edgecolor=colors[2], lw=1.8, label="Security dice")
    # plt.bar(states, C, width=0.7, color=(0,0,0,0), edgecolor="#824c71", lw=1.8, label="Security dice")

    # plt.bar(states, C, width=0.7, color=(0,0,0,0), edgecolor=colors[1], lw=1.8, label="Security dice")

    cst_agent = agent.ConstantAgent(NORMAL_DICE)
    C = estimate_cost(layout, circle, cst_agent)
    states = np.arange(len(C))+1
    plt.bar(states, C, width=0.7, color=(0,0,0,0), edgecolor=colors[4], lw=1.8, label="Normal dice")
    # plt.bar(states, C, width=0.7, color=(0,0,0,0), edgecolor="#dccca3", lw=1.8, label="Normal dice")


    C_opt = markovDecision(layout, circle)
    plt.bar(states, C_opt, width=0.7, color=(0,0,0,0), edgecolor=colors[1], lw=1.8, label="Optimal", tick_label=states)
    # plt.bar(states, C_opt, width=0.8, color=(0,0,0,0), edgecolor="#FEC89A", lw=1.5, label="Optimal", tick_label=states)
    # plt.bar(states, C_opt, width=0.7, color=(0,0,0,0), edgecolor="#90aa86", lw=1.8, label="Optimal", tick_label=states)

    plt.xlabel("States")
    plt.ylabel("Total expected cost")
    plt.legend()
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False) 
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.show()


if __name__ == '__main__':
    plot_cost()
