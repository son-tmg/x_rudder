import string

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

	def setTotalPlacedTokens(self,x,y):
		"""returns the total placed tokens"""
		return self._totalPlacedTokens
		
	def createGameGrid(self,rows,columns):
		"""Set gameGrid to a multidimensional 12x10 list and initiate elements to empty string."""
		self._gameGrid = [['x' for j in range(columns)] for i in range(rows)]

	def printGameGrid(self):
		"""prints the gameGrid """
		print("\n")
		for i in range(0,len(self._gameGrid)):
			row = i
			for j in range(0,len(self._gameGrid[i])):
				if(row == i) :
					print(10-i,end=" ")
					row = row - 1

				print(self._gameGrid[i][j],end=" ")
			
			print("\n")


			if i == 9:
				for i in range(13):
					print(string.ascii_uppercase[i],"", end = "")
			

	def checkState(self,Token):
		"""checks the current gamestate to see if there is a win or tie, based on last token added."""


if __name__ == "__main__":
	game = Game("","","",[],"")
	game.createGameGrid(10,12)
	game.printGameGrid()
