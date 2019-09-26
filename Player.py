class Player:
    """A Player in the Game"""

    def __init__(self, playerName, nbTokens, nbMoves, moveTime):
        """
        New instance of a PLayer

        playerName  Name of player, or named AI if Player vs AI is chosen.
        nbTokens    Number of tokens the current player has remaining to play.
        nbMoves     Number of moves the current player has played.
        moveTime    Time taken to make a move (Feature for AI player only).
        """

        self._playerName = playerName
        self._nbTokens = nbTokens
        self._nbMoves = nbMoves
        self._moveTime = moveTime

    def placeToken(self, Token, Token.position):
        """
        Method to Place an unused token on the game grid

        Token           Token object used to place on the game grid
        Token.position  Token coordinates to place on the game grid
        """

    def moveToken(self, Token, Token.position):
        """
        Method to move a used token on the game grid

        Token           Token object used to move on the game grid
        Token.position  Token coordinates to move on the game grid
        """
