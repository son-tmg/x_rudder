class Game:

	"""Represents a game session of X-Rudder"""
	
	def __init__(self,gameState,numberOfTotalTokens,totalTimeOfGame,totalPlacedTokens):
		self._gameState = gameState
		self._numberOfTotalTokens = numberOfTotalTokens
		self._gameGrid = self.createGameGrid()
		self._totalPlacedTokens = totalPlacedTokens

		print('\n','Inializiting new Game board.')
		self.printGameGrid()

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

	def setTotalPlacedTokens(self,x,y):
		"""returns the total placed tokens"""
		return self._totalPlacedTokens
		
	def createGameGrid(self):
		"""Set gameGrid to a multidimensional 12x10 list and initiate elements to empty string."""
		newGrid = [['x' for j in range(12)] for i in range(10)]
		return newGrid

	def printGameGrid(self):
		"""prints the gameGrid """
		print("\n")
		columns = ["A","B","C","D","E","F","G","H","I","J","K","L"]
		for i in range(0,10):
			row = i	
			for j in range(0,12):
				if(row == i) :
					print(10-i,end=" ")
					row = row - 1

				print('{:>5}'.format(self._gameGrid[i][j]),end=" ")
			
			print("\n")
			if i == 9:
				for i in range(len(columns)):
					print('{:>5}'.format(columns[i]),end=" ")				

		print("\n")





	def checkState(self,Token):
		"""checks the current gamestate to see if there is a win or tie, based on last token added."""


if __name__ == "__main__":
	game = Game(False,0,"",0)

