import numpy as np


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

	def update(self, state, action, reward, next_state):
		pass


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
