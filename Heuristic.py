import Game, Player, Token

class Heuristic:
    """The heuristic function used for the AI"""

    Score = 0
    maxDepth = 0

    def searchList(self, game, searchPosition, maxDepth = 1):
        """
        Method to get the list of positions to check

        searchPosition      Position coordinate to search and dictate the rest of potential moves
        maxDepth            maximum perimeter depth the function will look into to find the score
        """
        searchList = []
        y = searchPosition[0]
        x = searchPosition[1]
        maxScore = self.searchScore(game, searchPosition)

        if (0 <= y-maxDepth <= 9 and 0 <= x-maxDepth <= 11) and (0 <= y+maxDepth <= 9 and 0 <= x+maxDepth <= 11):
            for i in range(y-maxDepth, y+(maxDepth+1)):
                for j in range(x-maxDepth, x+(maxDepth+1)):
                    searchList.append([i,j])

            return self.searchScore(searchList)

        else:
            print("need to check and change maxDepth. WIP")

    def searchScore(self, game, searchPosition):
        """
        Method to get the score of each individual search positions

        game
        searchPosition
        """
        score1 = 0.2 * (15 - game.getPlayers()[0].get_nbTokens())
        score2 = 0.1 * (15 - game.getPlayers()[1].get_nbTokens())
        score3 = 0.2
