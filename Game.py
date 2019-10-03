
class Game:

	"""Represents a game session of X-Rudder"""
	
	def __init__(self,players,gameFinished,totalTimeOfGame,totalPlacedTokens,):
		"""
			players : list of the 2 players in the game
			gameFinished : True if game is finished (Win or Tie). False otherwise.
			totalTimeOfGame: total time of game
			gameGrid: game Grid containing all tokens in the game. 
			totalPlacedTokens : total placed tokens on board
		"""	

		self._players = players
		self._gameFinished = gameFinished
		self._gameGrid = self.createGameGrid()
		self._totalPlacedTokens = totalPlacedTokens

	def getgameFinished(self):
		"""returns the gameFinished"""
		return self._gameFinished

	def getGameGrid(self):
		"""returns the gameGrid"""
		return self._gameGrid

	def getTotalPlacedTokens(self):
		"""returns the total placed tokens"""
		return self._totalPlacedTokens

	def setgameFinished(self):
		"""sets the gameFinished"""
		return self._gameFinished

	def setGameGrid(self):
		"""returns the gameGrid"""
		return self._gameGrid

	def setTotalPlacedTokens(self,x,y):
		"""returns the total placed tokens"""
		return self._totalPlacedTokens
		
	def createGameGrid(self):
		"""Set gameGrid to a multidimensional 12x10 list and initiate elements to empty string.
			newGrid : a tuple of dictionaries. The tuples represent the rows, and each dictionary is a column 
						Keys: A - Z , Values: Tokens
		"""
		newGrid = (
					{{"A":" "},{"B":" "},{"C":" "},{"D":" "},{"E":" "},{"F":" "},{"G":" "},{"H":" "},{"I":" "},{"J":" "},{"K":" "},{"L":" "}},
					{{"A":" "},{"B":" "},{"C":" "},{"D":" "},{"E":" "},{"F":" "},{"G":" "},{"H":" "},{"I":" "},{"J":" "},{"K":" "},{"L":" "}},
					{{"A":" "},{"B":" "},{"C":" "},{"D":" "},{"E":" "},{"F":" "},{"G":" "},{"H":" "},{"I":" "},{"J":" "},{"K":" "},{"L":" "}},
					{{"A":" "},{"B":" "},{"C":" "},{"D":" "},{"E":" "},{"F":" "},{"G":" "},{"H":" "},{"I":" "},{"J":" "},{"K":" "},{"L":" "}},
					{{"A":" "},{"B":" "},{"C":" "},{"D":" "},{"E":" "},{"F":" "},{"G":" "},{"H":" "},{"I":" "},{"J":" "},{"K":" "},{"L":" "}},
					{{"A":" "},{"B":" "},{"C":" "},{"D":" "},{"E":" "},{"F":" "},{"G":" "},{"H":" "},{"I":" "},{"J":" "},{"K":" "},{"L":" "}},
					{{"A":" "},{"B":" "},{"C":" "},{"D":" "},{"E":" "},{"F":" "},{"G":" "},{"H":" "},{"I":" "},{"J":" "},{"K":" "},{"L":" "}},
					{{"A":" "},{"B":" "},{"C":" "},{"D":" "},{"E":" "},{"F":" "},{"G":" "},{"H":" "},{"I":" "},{"J":" "},{"K":" "},{"L":" "}},
					{{"A":" "},{"B":" "},{"C":" "},{"D":" "},{"E":" "},{"F":" "},{"G":" "},{"H":" "},{"I":" "},{"J":" "},{"K":" "},{"L":" "}},
					{{"A":" "},{"B":" "},{"C":" "},{"D":" "},{"E":" "},{"F":" "},{"G":" "},{"H":" "},{"I":" "},{"J":" "},{"K":" "},{"L":" "}}
				)
		print(newGrid[0])
		return newGrid

	def printGameGrid(self):

		"""prints the gameGrid as a 10 x 12 matrix"""
		print("\n")
		
		for i in range(self._gameGrid):
			




		# columns = ["A","B","C","D","E","F","G","H","I","J","K","L"]
		# for i in range(0,10):
		# 	row = i	
		# 	for j in range(0,12):
		# 		if(row == i) :
		# 			print(10-i,end=" ")
		# 			row = row - 1

		# 		print('{:>5}'.format(self._gameGrid[i][j]),end=" ")
			
		# 	print("\n")
		# 	if i == 9:
		# 		for i in range(len(columns)):
		# 			print('{:>5}'.format(columns[i]),end=" ")				

			print("\n")


	def checkState(self,Token):
		"""checks the current gameFinished to see if there is a win or tie, based on last token added."""


if __name__ == "__main__":
	g1 = Game("","","","")
