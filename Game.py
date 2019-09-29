class Game:

	""""Represents a game session of X-Rudder"""
	
	def __init__(self,gameState,numberOfTotalTokens,totalTimeOfGame,gameGrid,totalPlacedTokens):
		self._gameState = gameState
		self._numberOfTotalTokens = numberOfTotalTokens
		self._gameGrid = gameGrid
		self._totalPlacedTokens = totalPlacedTokens

	def getGameState(self):
		"""returns the gameState"""
		return self._gameState

	
	def getNumberOfTotalTokens(self):
		"""returns the number of total tokens"""
		return self._numberOfTotalTokens

	def getGameGrid(self):
		"""returns the gameGrid"""
		return self._gameGrid

	def getTotalPlacedTokens(self):
		"""returns the total placed tokens"""
		return self._totalPlacedTokens


	def setGameState(self):
		"""sets the gameState"""
		return self._gameState

	
	def setNumberOfTotalTokens(self):
		"""sets the number of total tokens"""
		return self._numberOfTotalTokens

	def setGameGrid(self):
		"""returns the gameGrid"""
		return self._gameGrid

	def setTotalPlacedTokens(self):
		"""returns the total placed tokens"""
		return self._totalPlacedTokens
		

	def checkState(self,Token):
		"""checks the current gamestate to see if there is a win or tie, based on last token added."""