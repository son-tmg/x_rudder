import Game, Token

class Heuristic:
    """The heuristic function used for the AI"""

    Score = 0
    maxDepth = 0

    def get_Score(self):
        """Return the score of the AI heuristic function"""
        return self._Score

    def get_Player(self):
        """Return the AI player"""
        return self._Player

    def get_maxDepth(self):
        """Return the specified max depth"""
        return self._maxDepth

    def searchList(self, searchPosition, maxDepth = 1):
        """
        Method to get the list of positions to check

        searchPosition      Position coordinate to search and dictate the rest of potential moves
        maxDepth            maximum perimeter depth the function will look into to find the score
        """
        searchList = []
        y = searchPosition[0]
        x = searchPosition[1]

        if (0 <= y-maxDepth <= 9 and 0 <= x-maxDepth <= 11) and (0 <= y+maxDepth <= 9 and 0 <= x+maxDepth <= 11):
            for i in range(y-maxDepth, y+(maxDepth+1)):
                for j in range(x-maxDepth, x+(maxDepth+1)):
                    searchList.append([i,j])

            self.searchScore(searchList)
        else:
            print("need to check and change maxDepth. WIP")

    def searchScore(self, searchList):
        """
        Method to get the score of each individual search positions

        searchList      List of all potential positions that can be played
        """

