import Game, Token

class Heuristic:
    """The heuristic function used for the AI"""

    def __init__(self, Player, maxDepth):
        """
        New instance of a heuristic function

        Score       Score of the potential move of the heuristic function
        Player      AI player containing all of its characteristics
        maxDepth    Maximum specified depth for the heuristic function

        """

        self._Score = 0
        self._Player = Player
        self._maxDepth = maxDepth

    def get_Score(self):
        """Return the score of the AI heuristic function"""
        return self._Score

    def get_Player(self):
        """Return the AI player"""
        return self._Player

    def get_maxDepth(self):
        """Return the specified max depth"""
        return self._maxDepth