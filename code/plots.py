import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

from snakes_and_ladders import SECURITY_DICE, NORMAL_DICE, RISKY_DICE
from value_iteration import markovDecision
from agent import ConstantAgent, OptimalAgent, RandomAgent
from simulation import estimate_cost
from graphics import plot_policy


colors = ["#e07a5f","#3d405b","#f2cc8f", "#83bcff", "#81b29a"]


def plot_cost(layout, circle, legend=True):
    agents = [OptimalAgent(layout, circle), ConstantAgent(SECURITY_DICE), ConstantAgent(NORMAL_DICE),
              ConstantAgent(RISKY_DICE), RandomAgent([SECURITY_DICE, NORMAL_DICE, RISKY_DICE])]
    labels = ["Optimal", "Security dice", "Normal dice", "Risky dice", "Random"]
    costs = [estimate_cost(layout, circle, pi) for pi in agents]
    states = np.arange(14)+1


    plt.figure(figsize=(6, 4), dpi=120)
    ax = plt.gca()

    C_th, _ = markovDecision(layout, circle)
    plt.plot(states, C_th, ls='--', color=colors[0], lw=1.8)


    for i, C in enumerate(costs):
        plt.plot(states, C, marker="o", color=colors[i], lw=1.8, label=labels[i])

    plt.xlabel("States")
    plt.ylabel("Total expected cost")
    plt.legend() if legend else ""
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False) 
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    plt.show()


def plot_cst_dice():
    layout = np.zeros(15)
    circle = True

    states = np.arange(14)+1
    dices = [SECURITY_DICE, NORMAL_DICE, RISKY_DICE]
    labels = ["Security dice", "Normal dice", "Risky dice"]

    plt.figure(figsize=(8.5, 3.5), dpi=120)
    dice_handles = []

    for j, circle in enumerate([False, True]):
        ax = plt.subplot(1, 2, j+1, sharey=ax if j == 1 else None)
        for i, dice in enumerate(dices):
            C_sim = estimate_cost(layout, circle, ConstantAgent(dice), n_episodes=1000)
            C_th, _ = markovDecision(layout, circle, actions=[dice])
        
            plt.plot(states, C_th, marker="o", color=colors[i+1])
            plt.plot(states, C_sim, marker="", color=colors[i+1], ls="--")

        plt.title("Circle = {}".format("True" if circle else "False"))
        plt.xlabel("States")
        plt.ylabel("Total expected cost") if j == 0 else ""
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False) 
        ax.yaxis.set_ticks_position('left')
        ax.xaxis.set_ticks_position('bottom')

        if j == 0:
            for i in range(len(dices)):
                dice_handle = Patch(color=colors[i+1], label=labels[i])
                dice_handles.append(dice_handle)

            sim_handle, = plt.plot([], [], label="Simulation", ls="--", color="gray")
            th_handle, = plt.plot([], [], label="Theory", marker="o", ls="-", color="gray")
            ax.legend(handles=[*dice_handles, sim_handle, th_handle])

    plt.tight_layout()
    plt.show()


def plot_policies(layouts, circles):
    n = len(layouts)
    fig, axs = plt.subplots(nrows=n//2, ncols=2, figsize=(11,2*n//2), dpi=130)
   
    if len(axs.shape) == 1:
        axs = axs[None,:]

    for i, layout in enumerate(layouts):
        _, pi = markovDecision(layout, circles[i])
        title="Config {}".format(i+1)
        plot_policy(axs[i//2,i%2], layout, circles[i], pi, title=title)

    plt.subplots_adjust(left=0.03, bottom=None, right=0.96, top=None, wspace=0.25, hspace=0.7)
    plt.show()


if __name__ == '__main__':
    # plot_cst_dice()

    layouts = np.zeros((2, 15), dtype=np.int)
    circles = [False, True]
    # plot_policies(layouts, circles)


    layouts = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0]
    ]
    circles = [False]*4
    # plot_policies(layouts, circles)


    layouts = [
        [0, 1, 0, 4, 0, 0, 0, 3, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 1, 0, 0, 0, 2, 0, 0, 4, 0]
    ]
    circles = [False, True]
    plot_policies(layouts, circles)

    for i, layout in enumerate(layouts):
        plot_cost(layout, circles[i], legend=True if i == 0 else False)
