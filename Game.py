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
			newGrid : a tuple of dictionaries. The tuples represent the rows, and each dictionary contains the pairs (Keys: A - Z , Values: Token object)
		"""
		newGrid = (
					{"A":None,"B":None,"C":None,"D":None,"E":None,"F":None,"G":None,"H":None,"I":None,"J":None,"K":None,"L":None},
					{"A":None,"B":None,"C":None,"D":None,"E":None,"F":None,"G":None,"H":None,"I":None,"J":None,"K":None,"L":None},
					{"A":None,"B":None,"C":None,"D":None,"E":None,"F":None,"G":None,"H":None,"I":None,"J":None,"K":None,"L":None},
					{"A":None,"B":None,"C":None,"D":None,"E":None,"F":None,"G":None,"H":None,"I":None,"J":None,"K":None,"L":None},
					{"A":None,"B":None,"C":None,"D":None,"E":None,"F":None,"G":None,"H":None,"I":None,"J":None,"K":None,"L":None},
					{"A":None,"B":None,"C":None,"D":None,"E":None,"F":None,"G":None,"H":None,"I":None,"J":None,"K":None,"L":None},
					{"A":None,"B":None,"C":None,"D":None,"E":None,"F":None,"G":None,"H":None,"I":None,"J":None,"K":None,"L":None},
					{"A":None,"B":None,"C":None,"D":None,"E":None,"F":None,"G":None,"H":None,"I":None,"J":None,"K":None,"L":None},
					{"A":None,"B":None,"C":None,"D":None,"E":None,"F":None,"G":None,"H":None,"I":None,"J":None,"K":None,"L":None},
					{"A":None,"B":None,"C":None,"D":None,"E":None,"F":None,"G":None,"H":None,"I":None,"J":None,"K":None,"L":None},
				)

		return newGrid

	def printGameGrid(self):

		"""prints the gameGrid as a 10 x 12 matrix"""
		print("\n")
		
		keys = ["A","B","C","D","E","F","G","H","I","J","K","L"]

		for i in range(len(self._gameGrid)):
			
			print(i, end="  ") # print row number and space

			for j in range(len(self._gameGrid[i])):
				print(self._gameGrid[i][keys[j]]," ",end="")

			print("\n")	# skip a line once a row has been printed for next row

			#when all rows have been printed, print a row of the keys 
			if i == 9:
				for i in range(12):
					print('{:>5}'.format(keys[i]),end=" ")	

		print("\n") #skip a line 


	def checkState(self,Token):
		"""checks the current gameFinished to see if there is a win or tie, based on last token added."""


if __name__ == "__main__":
	g1 = Game("","","","")
	g1.printGameGrid()