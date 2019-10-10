class Token:
    """A Token in the Game"""

    #class variables representing the unicode for black and white colored tokens
    white = 'u\u2588'
    black = 'u\u2591'


    def __init__(self, tokenColour, tokenPosition):
        """
        New instance of a Token

        tokenColour     String representing the Colour of the token, which could be white or black in unicode.
        tokenPosition   list representing Position of the token on the game grid. Always in pairs [i,j], where i is row and j is column
        """

        self._tokenColour = tokenColour
        self._tokenPosition = tokenPosition

    def get_tokenColour(self):
        """Return the colour of the token"""

        return self._tokenColour

    def get_tokenPosition(self):
        """Return the position of the token"""
        return self._tokenPosition

    def set_tokenColour(self,tokenColour):
        """Set the colour of the token"""
        self._tokenColour = tokenColour

    def set_tokenPosition(self,tokenPosition):
        """Set the position of the token"""
        self._tokenPosition = [tokenPosition[0],tokenPosition[1]]