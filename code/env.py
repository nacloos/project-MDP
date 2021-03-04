

class SnakesAndLadder:
	def __init__(self, layout, circle):
		"""
		Create a Snakes and Ladders game
		:param layout: layout of the game (see project instructions)
		:param circle: boolean, true if the player must land exactly on the final square to win
		"""
		self.state_space = list(range(1, 16)) # the squares of the game
		self.action_space = [1] # the dices
		

	def reset(self):
	    """
	    Restart the game
	    :return: initial state of the game
	    """
	    pass

	def step(self, action):
	    """
	    Perform one action in the environment
	    :param action: action taken by the agent
	    :return: next state, reward, a boolean which is true when the game is over
	    """
	    return self.state_space[0], 0, True
