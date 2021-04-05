import numpy as np

from snakes_and_ladders import *


class SnakesAndLaddersSim:
    """
    Simulation of the Snakes and Ladders game.
    """
    def __init__(self, layout, circle, random_start=False):
        """
        Create a Snakes and Ladders game
        :param layout: layout of the game (see project instructions)
        :param circle: boolean, true if the player must land exactly on the final square to win
        """
        self.layout = layout
        self.circle = circle
        self.random_start = random_start
        self.state_space = list(range(1, 16)) # the squares of the game
        self.action_space = [SECURITY_DICE, NORMAL_DICE, RISKY_DICE]
        self.current_state = START_STATE
        self.reward = 0
        self.tot_reward = 0

    def reset(self):
        """
        Restart the game
        """
        if self.random_start:
            self.current_state = np.random.randint(14)
        else:
            self.current_state = START_STATE
        return self.current_state

    def movement(self, squares):
        if self.current_state == JUNCTION_STATE: # manage junction
            if squares != 0:
                roll = np.random.randint(2)
                if roll == 0:
                    self.current_state = FAST_LANE_START + squares - 1
                else:
                    self.current_state += squares    
        else:
            next_state = self.current_state + squares
            if (next_state > 9) and (self.current_state <= 9): # manage gap between 10 and 15
                next_state += 4
            if self.circle & (next_state > FINAL_STATE): # manage after last state if circle
                self.reward += 1
                self.current_state = START_STATE
            else:
                if next_state > FINAL_STATE: # only consider to finish if not circle
                    self.current_state = FINAL_STATE
                else:
                    self.current_state = next_state

    def trap(self):
        if self.layout[self.current_state] == RESTART_TRAP:
            self.current_state = START_STATE
        elif self.layout[self.current_state] == PENALTY_TRAP:
            if self.current_state in [10, 11, 12]:
                self.current_state -= 10
            else:
                self.current_state -= 3
            if self.current_state < 0:
                self.current_state = 0
        elif self.layout[self.current_state] == PRISON_TRAP:
            self.reward -= 1
        elif self.layout[self.current_state] == GAMBLE_TRAP:
            self.current_state = np.random.randint(15)

    def step(self, action):
        """
        Perform one action in the environment
        :param action: action taken by the agent
        :return: next state, reward, a boolean which is true when the game is over
        """
        self.reward = -1
        if action == SECURITY_DICE:
            squares = np.random.randint(2)
            trap_chance = 1
        elif action == NORMAL_DICE:
            squares = np.random.randint(3)
            trap_chance = np.random.randint(2)
        elif action ==  RISKY_DICE:
            squares = np.random.randint(4)
            trap_chance = 0

        self.movement(squares)
        # active the trap with certain proba according to the dice
        if (trap_chance == 0) and (self.current_state < FINAL_STATE):
            self.trap()
        done = self.current_state >= FINAL_STATE

        return self.current_state, self.reward, done
