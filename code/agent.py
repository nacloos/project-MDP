import numpy as np

from value_iteration import markovDecision

class BaseAgent:
	"""
	Base agent class specifying the interface of an agent object
	"""
	def __init__(self):
		pass

	def select_action(self, state):
		"""
		:param state: state of the environment
		:return: action
		"""
		return None

	def update(self, state, action, reward, next_state):
		"""
		Update the action selection using a learning rule
		"""
		pass


class RandomAgent(BaseAgent):
	def __init__(self, action_space):
		self.action_space = action_space

	def select_action(self, state):
		return np.random.choice(self.action_space)


class ConstantAgent(BaseAgent):
    def __init__(self, action):
        self.action = action

    def select_action(self, state):
        return self.action


class OptimalAgent(BaseAgent):
    def __init__(self, layout, circle):
        _, self.pi = markovDecision(layout, circle)

    def select_action(self, state):
        return self.pi[state]
        

class QLearningAgent(BaseAgent):
	def __init__(self):
		pass

	def select_action(self, state):
		return None

	def update(self, state, action, reward, next_state):
		"""
		Update the value function
		"""
		pass
