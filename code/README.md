## Description of the scripts

#### Theoretical part

* *snakes_and_ladders.py* provides the SnakesAndLaddersProb class which is used to get the probability transition function for the Snakes and Ladders game.
* *value_iteration.py* implements the **markovDecision** function where the value iteration algorithm is used to compute the optimal strategy. It uses the probability transition function from SnakesAndLaddersProb.

#### Simulation part

* *snakes_and_ladders_sim.py* provides the SnakesAndLaddersSim class which is used to simulate the game.
* *agent.py* contains various agent classes that can be used to play the game.
* *simulation.py* simulates the interaction between an agent and the game, it is used to compute empirically the cost and the transition probabilities.

#### Misc

* *tests.py* contains some tests to compare the transition probabilities of SnakesAndLaddersProb with those estimated with simulations, same for the total expected costs.
* *plots.py* reproduces the plots of the report.
* *graphics.py* displays the game and the optimal policy.

