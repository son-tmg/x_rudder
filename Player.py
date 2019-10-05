import Token

class Player:
    """A Player in the Game"""

    def __init__(self, playerName):
        """
        New instance of a PLayer

        playerName  Name of player, or named AI if Player vs AI is chosen.
        nbTokens    Number of tokens the current player has remaining to play.
        nbMoves     Number of moves the current player has played.
        moveTime    Time taken to make a move (Feature for AI player only).
        """

        self._playerName = playerName
        self._playerColour = ""
        self._nbTokens = 15
        self._nbMoves = 0
        self._moveTime = 0

    def get_playerName(self):
        """Return the name of the player"""
        return self._playerName

    def get_playerColour(self):
        """Return the colour of the player"""
        return self._playerColour

    def get_nbTokens(self):
        """Return the number of tokens of the player"""
        return self._nbTokens

    def get_nbMoves(self):
        """Return the number of moves of the player"""
        return self._nbMoves

    def get_moveTime(self):
        """Return the time took for the player/AI to make a move"""
        return self._moveTime

    def InitializeTokenList(self):
        """Initializes the token list of the player"""

        PlayerTokens = []
        for i in range(15):
            PlayerTokens.append(Token(self.playerColour, 0)) #The token coordinate argument is set to 0, need to be changed WIP


    def placeToken(self, Token, position):
        """
        Method to Place an unused token on the game grid

        Token           Token object used to place on the game grid
        Token.position  Token coordinates to place on the game grid
        """
        if Token.placed == True:
            x = input(print("Token has already been placed. Would you like to move it (Yes or No)"))
            if x.casefold() == "yes":
                self.moveToken(Token, position) #WIP
            else:
                y = input(print("Choose another Token."))
                self.placeToken(y, [1,"A"])   #For coordinate, place a list as the argument, 1st arg. being 1-10, 2nd being A-L
        else:
            updateGameGrid(-position)  #WIP


    def moveToken(self, Token, position):
        """
        Method to move a used token on the game grid

        Token           Token object used to move on the game grid
        Position        Token coordinates to move on the game grid
        """
