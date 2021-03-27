import numpy as np

from snakes_and_ladders import SnakesAndLaddersProb, SECURITY_DICE, NORMAL_DICE, RISKY_DICE
import transition_prob
import simulation
from value_iteration import 


layouts = [
    np.zeros(15),
    np.array([0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    np.array([0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    np.array([0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]),
    np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0]),
    np.array([0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0]),
    # np.array([0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 2, 0, 2, 0]),
    # np.array([0, 2, 0, 1, 1, 2, 0, 2, 1, 0, 1, 2, 2, 1, 0]),
    np.array([0, 0, 4, 4, 0, 0, 0, 4, 0, 0, 0, 4, 4, 0, 0]),
    np.array([0, 3, 1, 4, 2, 0, 1, 4, 2, 3, 0, 4, 1, 0, 0])
]

def test_prob(layout, circle, dice):
    # security dice
    # if dice == SECURITY_DICE:
    #     P1 = transition_prob.propTranSec()
    # elif dice == NORMAL_DICE:
    #     P1 = transition_prob.propTransNoAct(layout, circle)
    # else:
    #     print("Dice not implemented !")

    env = SnakesAndLaddersProb(layout, circle)
    P2 = np.array([env.p(s, dice)[0] for s in range(15)])

    P3 = simulation.estimate_prob(layout, circle, dice, n_episodes=int(1e4))
    # P3 = P2
    P1 = P2

    passed = True
    for s in range(15):
        if not np.isclose(np.sum(P1[s]), 1):
            print("\nRadia: row not summing to 1 for state {}".format(s))
            print(*P1[s])
        if not np.isclose(np.sum(P2[s]), 1):
            print("\nNathan: row not summing to 1 for state {}".format(s))
            print(*P2[s])
        if not np.isclose(np.sum(P3[s]), 1):
            print("\nAdrien: row not summing to 1 for state {}".format(s))
            print(*P3[s])

        if not np.allclose(P1[s], P2[s]) or not np.allclose(P1[s], P3[s], atol=0.05) or not np.allclose(P2[s], P3[s], atol=0.05):
            print("\nNot the same transition probability for state {}:".format(s))
            # print("Radia:", *P1[s])
            print("Nathan:", *P2[s])
            print("Adrien:", *P3[s])
            passed = False

    return passed


# def test_cost(layout, circle, dice):
#     C = markovDecision(layout, circle)


if __name__ == '__main__':
    for i, layout in enumerate(layouts):
        print("===== Test layout {} =====".format(i))
        print("=== Security dice: ")
        print("= Circle false: ", end="")
        passed = test_prob(layout, False, SECURITY_DICE)
        print("OK") if passed else print("FAILED\n")
        print("= Circle true: ", end="")
        passed = test_prob(layout, True, SECURITY_DICE)
        print("OK") if passed else print("FAILED\n")
        
        print("=== Normal dice: ")
        print("= Circle false: ", end="")
        passed = test_prob(layout, False, NORMAL_DICE)
        print("OK") if passed else print("FAILED\n")
        print("= Circle true: ", end="")
        passed = test_prob(layout, True, NORMAL_DICE)
        print("OK") if passed else print("FAILED\n")

        print("=== Risky dice: ")
        print("= Circle false: ", end="")
        passed = test_prob(layout, False, RISKY_DICE)
        print("OK") if passed else print("FAILED\n")
        print("= Circle true: ", end="")
        passed = test_prob(layout, True, RISKY_DICE)
        print("OK") if passed else print("FAILED")
        print()
