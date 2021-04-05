import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.legend_handler import HandlerBase
from matplotlib.text import Text
from matplotlib.legend import Legend
from matplotlib.lines import Line2D

from value_iteration import markovDecision


dice_label = {
    1: " S ",
    2: " N ",
    3: " R "
}


# traps_color = [None, "#555b6e", "#A7C7E7", "#bee3db", "#ffd6ba"]
traps_color = [None, "#555b6e", "tab:blue", "tab:green", "tab:orange"]
traps_label = [None, "Restart", "Penalty", "Prison", "Gamble"]



def plot_policy(ax, layout, circle, pi, title=""):
    pi = [dice_label[int(a)] for a in pi]


    width = 10
    height = 10
    spacing = 5
    total_width = 10*(width+spacing)

    for i in range(15):
        edgecolor = traps_color[layout[i]]
        linewidth = 0 if layout[i] == 0 else 1.5
        bbox = dict(boxstyle='Square, pad=0.5', ec=edgecolor, facecolor='#f6f4f4', lw=linewidth)

        if circle:
            bbox['boxstyle'] = 'Circle, pad=0.5'

        if i < 10:
            x = i*(width+spacing) / total_width
            y = 0.7
            s = pi[i]
        elif i == 14:
            x = 1.02
            y = 0.7
            s = "Goal"
        else:
            x = 1.7*(i-10)*(width+spacing) / total_width + 0.35
            y = 0.2
            s = pi[i]

        ax.text(x, y, s, color="#3d405b", ha="center", va='center', bbox=bbox, transform=ax.transAxes)

    # ax.axis('equal')
    ax.axis('off')
    ax.set_title(title)
    # ax.set_title("Circle = {}".format("True" if circle else "False"))


class TextHandlerB(HandlerBase):
    #https://stackoverflow.com/questions/27174425/how-to-add-a-string-as-the-artist-in-matplotlib-legend
    def create_artists(self, legend, text ,xdescent, ydescent,
                    width, height, fontsize, trans):
        tx = Text(width/2.,height/2, text, fontsize=fontsize,
                  ha="center", va="center")
        return [tx]


def plot_traps_legend():
    plt.subplot(1, 3, 1)
    Legend.update_default_handler_map({str : TextHandlerB()})
    plt.legend(handles=["S", "N", "R"], labels=["Security", "Normal", "Risky"], title="Dices", loc='center')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    # handle1 = mpatches.FancyBboxPatch((0,0), 10, 10, boxstyle='Square, pad=0.5', facecolor='#f6f4f4', lw=0, label="False")
    # handle2 = mpatches.FancyBboxPatch((0,0), 10, 10, boxstyle='Circle, pad=0.5', facecolor='#f6f4f4', lw=0, label="False")
    handle1, = Line2D([0], [0], marker='s', color='w', label='False', markerfacecolor='lightgray', markersize=11),
    handle2, = Line2D([0], [0], marker='o', color='w', label='True', markerfacecolor='lightgray', markersize=11),
    plt.legend(handles=[handle1, handle2], loc='center', title='Circle')
    plt.axis('off')


    plt.subplot(1, 3, 3)
    handles = []
    for i, label in enumerate(traps_label):
        if label:
            patch = mpatches.Patch(label=label, color=traps_color[i])
            handles.append(patch)
    plt.legend(handles=handles, loc='center', title="Traps")
    plt.axis('off')




if __name__ == '__main__':
    circle = True
    layout = np.zeros(15, dtype=np.int)
    # layout[8] = 1
    # layout[1] = 2
    # layout[12] = 3
    # layout[10] = 4
    # layout[1] = 3
    # layout[13] = 1
    layout[9] = 1

    # pi = np.full(15, 2)
    _, pi = markovDecision(layout, circle)
    print(pi)

    # fig = plt.figure(figsize=(6, 2), dpi=130)
    # ax = plt.gca()
    # plot_policy(ax, layout, circle, pi)
    # plt.show()

    fig = plt.figure(figsize=(6, 2), dpi=130)
    ax = plt.gca()
    plot_traps_legend()
    plt.show()
