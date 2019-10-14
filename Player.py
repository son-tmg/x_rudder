import Game, Token

class Player:
    """A Player in the Game"""

    def __init__(self, playerName, playerColour):
        """
        New instance of a PLayer

        playerName      Name of player, or named AI if Player vs AI is chosen.
        playerColour    Colour of the player and their tokens
        playerTokens    List of tokens belonging to the player
        nbTokens        Number of tokens the current player has remaining to play.
        nbMoves         Number of moves the current player has played.
        moveTime        Time taken to make a move (Feature for AI player only).
        """

        self._playerName = playerName
        self._playerColour = playerColour
        self._playerTokens = []
        self._nbTokens = 15
        self._nbMoves = 0
        self._moveTime = 0

    def get_playerName(self):
        """Return the name of the player"""
        return self._playerName

    def get_playerColour(self):
        """Return the colour of the player"""
        return self._playerColour

    def get_playerTokens(self):
        """Return the colour of the player"""
        return self._playerTokens

    def get_nbTokens(self):
        """Return the number of tokens of the player"""
        return self._nbTokens

    def get_nbMoves(self):
        """Return the number of moves of the player"""
        return self._nbMoves

    def get_moveTime(self):
        """Return the time took for the player/AI to make a move"""
        return self._moveTime

    #----------------------------------------------------------------------------------------------------

    def InitializeTokenList(self):
        """Initializes the token list of the player"""

        for i in range(15):
            self._playerTokens.append(Token.Token(self._playerColour, [None, None]))

    def placeToken(self, game, playerTokens, newPosition):
        """
        Method to Place an unused token on the game grid

        playerTokens    List of tokens belonging to the player
        position        Position coordinate to place the token
        """
        if not playerTokens:
            position = input("No more tokens are available to place. Please indicate which token from the grid" +
                             " you would like to move by inputting its position coordinate (e.g. 1,A): ").split(",")
            newPosition = input("Now input the position coordinate that you would like to move the token to (e.g. 1,A): ").split(",")
            self.moveToken(game, position, newPosition)
        else:
            token = playerTokens[0]
            playerTokens.pop(0)
            if game._gameGrid[newPosition[0]][newPosition[1]] is None:
                game.updateGameGrid(token, newPosition, "placement")
                game.checkState(token, "placement")
            else:
                new_position = input("The position you have requested to add your token at already has a token on it. " +
                                     "Please input a new position coordinate (e.g. 1,A): ").split(",")
                self.placeToken(game, playerTokens, newPosition)

    def moveToken(self, game, oldPosition, newPosition):
        """
        Method to move a used token on the game grid

        Token           Token object used to move on the game grid
        Position        Token coordinates to move on the game grid
        """
        token = playerTokens[0]
        playerTokens.pop(0)

        if game._gameGrid[newPosition[0]][newPosition[1]] is None:
            game.updateGameGrid(token, newPosition, "placement")
            game.checkState(token)

            """if game._gameGrid[oldPosition[0]][oldPosition[1]] is None:
            Position1, Position2 = "", ""
            print(
                "The token you have requested to move is not at the specified location. Please re-enter a new coordinate of a token currently placed on the grid.")
            while Position1 not in gameStart.rows:
                Position1 = input(
                    "\nPlease pick which row you would like to place your token in (Select from 1 to 10): ")
            oldPosition.append(10 - int(Position1))
            while Position2 not in gameStart.columns:
                Position2 = input(
                    "\nPlease pick which column you would like to place your token in (Select from A to L): ").lower()
            Position2 = ord(Position2.lower()) - 97
            oldPosition.append(Position2)"""