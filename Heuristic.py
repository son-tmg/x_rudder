import Game, Player, Token

class Heuristic:
    """The heuristic function used for the AI"""

    def searchList(self, game, searchPosition, maxDepth = 1):
        """
        Method to get the list of positions to check, returning the positions which have the highest evaluation

        game                The game that is being played on
        searchPosition      The current grid position being evaluated, with its specified perimeter positions
        maxDepth            The maximum perimeter depth the function will look into to find the score
        """
        y = searchPosition[0]
        x = searchPosition[1]
        maxList = []

        if game.getGameGrid()[y][x] is None:
            maxScore = self.searchScore(game, searchPosition)
            maxList.append(searchPosition)
        else:
            maxScore = 0

        #if (0 <= y-maxDepth <= 9 and 0 <= x-maxDepth <= 11) and (0 <= y+maxDepth <= 9 and 0 <= x+maxDepth <= 11):
        for i in range(y-maxDepth, y+(maxDepth+1)):
            for j in range(x-maxDepth, x+(maxDepth+1)):
                if (0 <= i <= 9 and 0 <= j <= 11):
                    if self.searchScore(game, [i, j]) > maxScore:
                        maxScore = self.searchScore(game, [i, j])
                        for element in maxList:
                            maxList.pop()
                        maxList.append([i,j])
                    elif self.searchScore(game, [i, j]) == maxScore:
                        maxList.append([i, j])

        return maxList

    def searchScore(self, game, searchPosition):
        """
        Method to get the score of each individual search positions

        game                The game that is being played on
        searchPosition      The current grid position being evaluated
        """
        y = searchPosition[0]
        x = searchPosition[1]
        score1 = 0.2 * (15 - game.getPlayers()[0].get_nbTokens())
        score2 = -0.1 * (15 - game.getPlayers()[1].get_nbTokens())
        score3 = 0
        score4 = 0

        for i in range(y - 1, y + 2):
            for j in range(x - 1, x + 2):
                if (0 <= i <= 9 and 0 <= j <= 11) and (game.getGameGrid()[i][j] is not None):
                    if game.getGameGrid()[i][j].get_tokenColour() == game.getPlayers()[0].get_playerColour():
                        score3 += 1
                    else:
                        score4 += 1

        score3 *= 0.2
        score4 *= -0.1

        #Addition of score5 from heuristic feature 5 * weight of function 5
        return (score1 + score2 + score3 + score4)
