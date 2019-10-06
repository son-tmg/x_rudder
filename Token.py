class Token:
    """A Token in the Game"""

    def __init__(self, tokenColour, tokenPosition):
        """
        New instance of a Token

        tokenColour     Colour of the token, which could be black or red
        tokenPosition   Position of the token on the game grid
        """

        self._tokenColour = tokenColour
        self._tokenPosition = tokenPosition

    def get_tokenColour(self):
        """Return the colour of the token"""

        return self._tokenColour

    def get_tokenPosition(self):
        """Return the position of the token"""
        return self._tokenPosition
