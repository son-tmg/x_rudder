class Node:
    """A node in the Minimax Algorithm"""
    def __init__(self, score, position):
        """
        New instance of a node

        Score     Represents the heuristic score
        Position   Represents the position at which the token that's being evaluated is placed
        """
        self._score = score
        self._position = position
        self._extra = None

    def get_score(self):
        """Return the score of the node"""
        return self._score

    def get_position(self):
        """Return the position of the node"""
        return self._position

    def get_extra(self):
        """Return the score of the node"""
        return self._extra

    def set_score(self,score):
        """Set the score of the node"""
        self._score = score

    def set_position(self,position):
        """Set the position of the node"""
        self._position = [position[0], position[1]]

    def set_extra(self,extra):
        """Set the score of the node"""
        self._extra = extra

    def append_position(self, position):
        self._position.append(position)