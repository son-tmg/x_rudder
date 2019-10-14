import Token
import Player

class Game:

	"""Represents a game session of X-Rudder"""
	
	"""-----*******************************************-----Color for black : print(u'\u2588',u'\u2591')----*******************************************--"""


	def __init__(self,players):
		"""
			players : list of the 2 players in the game
			gameFinished : True if game is finished (Win or Tie). False otherwise.
			totalTimeOfGame: total time of game
			gameGrid: game Grid containing all tokens in the game. 
			totalPlacedTokens : total placed tokens on board
		"""	

		self._players = players
		self._gameFinished = False
		self._gameGrid = [ 
					[None,None,None,None,None,None,None,None,None,None,None,None],
					[None,None,None,None,None,None,None,None,None,None,None,None],
					[None,None,None,None,None,None,None,None,None,None,None,None],
					[None,None,None,None,None,None,None,None,None,None,None,None],
					[None,None,None,None,None,None,None,None,None,None,None,None],
					[None,None,None,None,None,None,None,None,None,None,None,None],
					[None,None,None,None,None,None,None,None,None,None,None,None],
					[None,None,None,None,None,None,None,None,None,None,None,None],
					[None,None,None,None,None,None,None,None,None,None,None,None],
					[None,None,None,None,None,None,None,None,None,None,None,None],
			]

			

		self._totalPlacedTokens = 0
		self._totalTimeOfGame = 0

	def getgameFinished(self):
		"""returns the gameFinished"""
		return self._gameFinished

	def getGameGrid(self):
		"""returns the gameGrid"""
		return self._gameGrid

	def getTotalPlacedTokens(self):
		"""returns the total placed tokens"""
		return self._totalPlacedTokens

	def setgameFinished(self,gameFinished):
		"""sets the gameFinished status """
		self._gameFinished = gameFinished

	def setGameGrid(self,gameGrid):
		"""sets the gameGrid"""
		self._gameGrid = gameGrid

	def setTotalPlacedTokens(self,totalPlacedTokens):
		"""sets the total placed tokens"""
		self._totalPlacedTokens = totalPlacedTokens
		
	def printGameGrid(self):
		"""prints the gameGrid as a 10 x 12 matrix"""
		keys = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]

		print("\n")

		for i in range(len(self._gameGrid)):

			print(10-i, end="  ") # print row number and space

			for j in range(len(self._gameGrid[i])):
				if self._gameGrid[i][j] is None:
					print(self._gameGrid[i][j], " ", end="")
				else:
					print(self._gameGrid[i][j].get_tokenColour(), " ", end="")

			print("\n")	# skip a line once a row has been printed for next row

			#when all rows have been printed, print a row of the keys
			if i == 9:
				for i in range(12):
					print('{:>5}'.format(keys[i]),end=" ")

		return "\n" #skip a line

	def updateGameGrid(self, token, newPosition, moveType):
		"""
		updates game grid with new token or move.
		if placing token:get coordinates of old tokenset game grid position
		if moving token : get old position and set that GameGrid position to None, then get new position, set it for token and set that new gameGrid position to token.
		"""

		if moveType == "placement":
			i = newPosition[0]
			j = newPosition[1]
			token.set_tokenPosition(newPosition)
			self._gameGrid[i][j] = token
		elif moveType == "movement":
			i = token.get_tokenPosition[0]
			j = token.get_tokenPosition[1]
			self._gameGrid[i][j] = None

			k = newPosition[0]
			l = newPosition[1]
			token.set_tokenPosition(newPosition)
			self._gameGrid[k,l] = token

		self.printGameGrid()


	def checkState(self,token,moveType):
		"""checks to see if the last token that was placed or moved generated one of the 5 wining states.
		
			Token : token of a player
			turnType : move or place
			return : nothing
		"""

		i = token.get_tokenPosition()[0]	#row
		j = token.get_tokenPosition()[1]	#column

		"""WIP : What happens if we crossed out an oppsing X, but move one of the 2 crossing tokens and generate a win for the other player ? """

		#Refactor into 2 seperate functions : checking which of the 5 cases and


		#center
		if ( 1<=i<=8 and 1<=j<=10):
			if (
				self._gameGrid[i+1][j+1] != None and self._gameGrid[i+1][j+1].get_tokenColour() == token.get_tokenColour() and
				self._gameGrid[i+1][j-1] != None and self._gameGrid[i+1][j-1].get_tokenColour() == token.get_tokenColour() and
				self._gameGrid[i-1][j+1] != None and self._gameGrid[i-1][j+1].get_tokenColour() == token.get_tokenColour() and 
				self._gameGrid[i-1][j-1] != None and self._gameGrid[i-1][j-1].get_tokenColour() == token.get_tokenColour()
			):
				if (
					self._gameGrid[i][j-1] == None or self._gameGrid[i][j-1].get_tokenColour() == token.get_tokenColour() or 
					self._gameGrid[i][j+1] == None or self._gameGrid[i][j+1].get_tokenColour() == token.get_tokenColour()
					):
						self.setgameFinished(True)

		#top left						
		if (0<=i<=7 and 0<=j<=9):		
			if(
				self._gameGrid[i][j+2] != None and self._gameGrid[i][j+2].get_tokenColour() == token.get_tokenColour() and
				self._gameGrid[i+1][j+1] != None and self._gameGrid[i+1][j+1].get_tokenColour() == token.get_tokenColour() and
				self._gameGrid[i+2][j] != None and self._gameGrid[i+2][j].get_tokenColour() == token.get_tokenColour() and 
				self._gameGrid[i+2][j+2] != None and self._gameGrid[i+2][j+2].get_tokenColour() == token.get_tokenColour()
			):
				if (
					self._gameGrid[i+1][j] == None or self._gameGrid[i+1][j].get_tokenColour() == token.get_tokenColour() or
					self._gameGrid[i+1][j+2] == None or self._gameGrid[i+1][j+2].get_tokenColour() == token.get_tokenColour()
					):
						self.setgameFinished(True)

		#top right
		if (0<=i<=7 and 2<=j<=11):		
			if (
				self._gameGrid[i][j-2] != None and self._gameGrid[i][j-2].get_tokenColour() == token.get_tokenColour() and
				self._gameGrid[i+1][j-1] != None and self._gameGrid[i+1][j-1].get_tokenColour() == token.get_tokenColour() and
				self._gameGrid[i+2][j-2] != None and self._gameGrid[i+2][j-2].get_tokenColour() == token.get_tokenColour() and 
				self._gameGrid[i+2][j] != None and self._gameGrid[i+2][j].get_tokenColour() == token.get_tokenColour()
			):
				if (
					self._gameGrid[i+1][j] == None or self._gameGrid[i+1][j].get_tokenColour() == token.get_tokenColour() or
					self._gameGrid[i+1][j-2] == None or self._gameGrid[i+1][j-2].get_tokenColour() == token.get_tokenColour()
					):
						self.setgameFinished(True)
		
		#bottom left
		if (2<=i<=9 and 0<=j<=9):
			if (
				self._gameGrid[i-2][j] != None and self._gameGrid[i-2][j].get_tokenColour() == token.get_tokenColour() and
				self._gameGrid[i][j+2] != None and self._gameGrid[i][j+2].get_tokenColour() == token.get_tokenColour() and
				self._gameGrid[i-1][j+1] != None and self._gameGrid[i-1][j+1].get_tokenColour() == token.get_tokenColour() and 
				self._gameGrid[i-2][j+2] != None and self._gameGrid[i-2][j+2].get_tokenColour() == token.get_tokenColour()
			):
				if (
					self._gameGrid[i-1][j] == None or self._gameGrid[i-1][j].get_tokenColour() == token.get_tokenColour() or
					self._gameGrid[i-1][j+2] == None or self._gameGrid[i-1][j+2].get_tokenColour() == token.get_tokenColour()
					):
						self.setgameFinished(True)

		#bottom right			
		if (2<=i<=9 and 2<=j<=11):		
			if (
				self._gameGrid[i-2][j] != None and self._gameGrid[i-2][j].get_tokenColour() == token.get_tokenColour() and
				self._gameGrid[i-1][j-1] != None and self._gameGrid[i-1][j-1].get_tokenColour() == token.get_tokenColour() and
				self._gameGrid[i][j-2] != None and self._gameGrid[i][j-2].get_tokenColour() == token.get_tokenColour() and 
				self._gameGrid[i-2][j-2] != None and self._gameGrid[i-2][j-2].get_tokenColour() == token.get_tokenColour()
			):
				if (
					self._gameGrid[i-1][j] == None or self._gameGrid[i-1][j].get_tokenColour() == token.get_tokenColour() or
					self._gameGrid[i-1][j-2] == None or self._gameGrid[i-1][j-2].get_tokenColour() == token.get_tokenColour()
					):
						self.setgameFinished(True)

		#if none of the 5 winning configurations were found, this means the player has not won yet and the game continues.