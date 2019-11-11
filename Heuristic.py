import Game, Player, Token, random, Node, copy

class Heuristic:
    """The heuristic function used for the AI"""

    @staticmethod
    def searchList(game, searchPosition, maxDepth = 1):
        """
        Method to get the list of positions to check, returning the positions which have the highest evaluation

        game                The game that is being played on
        searchPosition      The current grid position being evaluated, with its specified perimeter positions
        maxDepth            The maximum perimeter depth the function will look into to find the score
        """

        def searchScore(game, searchPosition):
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
            score5 = 0.4 * getNumberOfWinningConfigurations(searchPosition, game)

            for i in range(y - 1, y + 2):
                for j in range(x - 1, x + 2):
                    if (0 <= i <= 9 and 0 <= j <= 11) and (game.getGameGrid()[i][j] is not None):
                        if game.getGameGrid()[i][j].get_tokenColour() == game.getPlayers()[0].get_playerColour():
                            score3 += 1
                        else:
                            score4 += 1

            score3 *= 0.2
            score4 *= -0.1

            # Addition of score5 from heuristic feature 5 * weight of function 5
            return (score1 + score2 + score3 + score4 + score5)

        def getNumberOfWinningConfigurations(searchPosition, game):
            """
                Returns the number of winning configurations for the searchPosition.
                This is determined by determining how many of the 5 winning possible winning configurations can be generated (Center, TL, TR, BL, BR)
                if the token was placed at that position

                searchPosition : Current gameGrid position being evaluated for its position.
                game : The game that is being played on

            """
            numberOfWinningConfigurations = 0
            gameGrid = game.getGameGrid()
            i = searchPosition[1]
            j = searchPosition[0]

            # Center
            if (1 <= i <= 8 and 1 <= j <= 10):
                if (
                        (gameGrid[i + 1][j + 1] == None or gameGrid[i + 1][j + 1].get_tokenColour() ==
                         game.getPlayers()[0].get_playerColour()) and
                        (gameGrid[i + 1][j - 1] == None or gameGrid[i + 1][j - 1].get_tokenColour() ==
                         game.getPlayers()[0].get_playerColour()) and
                        (gameGrid[i - 1][j + 1] == None or gameGrid[i - 1][j + 1].get_tokenColour() ==
                         game.getPlayers()[0].get_playerColour()) and
                        (gameGrid[i - 1][j - 1] == None or gameGrid[i - 1][j - 1].get_tokenColour() ==
                         game.getPlayers()[0].get_playerColour())
                ):
                    if (
                            (gameGrid[i][j - 1] == None or gameGrid[i][j - 1].get_tokenColour() ==
                             game.getPlayers()[0].get_playerColour()) and
                            (gameGrid[i][j + 1] == None or gameGrid[i][j + 1].get_tokenColour() ==
                             game.getPlayers()[0].get_playerColour())

                    ):
                        numberOfWinningConfigurations += 1

            # top left
            if (0 <= i <= 7 and 0 <= j <= 9):
                if (
                        (gameGrid[i][j + 2] == None or gameGrid[i][j + 2].get_tokenColour() ==
                         game.getPlayers()[0].get_playerColour()) and
                        (gameGrid[i + 1][j + 1] == None or gameGrid[i + 1][j + 1].get_tokenColour() ==
                         game.getPlayers()[0].get_playerColour()) and
                        (gameGrid[i + 2][j] == None or gameGrid[i + 2][j].get_tokenColour() ==
                         game.getPlayers()[0].get_playerColour()) and
                        (gameGrid[i + 2][j + 2] == None or gameGrid[i + 2][j + 2].get_tokenColour() ==
                         game.getPlayers()[0].get_playerColour())
                ):
                    if (
                            (gameGrid[i + 1][j] == None or gameGrid[i + 1][j].get_tokenColour() ==
                             game.getPlayers()[0].get_playerColour()) and
                            (gameGrid[i + 1][j + 2] == None or gameGrid[i + 1][j + 2].get_tokenColour() ==
                             game.getPlayers()[0].get_playerColour())
                    ):
                        numberOfWinningConfigurations += 1

            # top right
            if (0 <= i <= 7 and 2 <= j <= 11):
                if (
                        (gameGrid[i][j - 2] == None or gameGrid[i][j - 2].get_tokenColour() ==
                         game.getPlayers()[0].get_playerColour()) and
                        (gameGrid[i + 1][j - 1] == None or gameGrid[i + 1][j - 1].get_tokenColour() ==
                         game.getPlayers()[0].get_playerColour()) and
                        (gameGrid[i + 2][j - 2] == None or gameGrid[i + 2][j - 2].get_tokenColour() ==
                         game.getPlayers()[0].get_playerColour()) and
                        (gameGrid[i + 2][j] == None or gameGrid[i + 2][j].get_tokenColour() ==
                         game.getPlayers()[0].get_playerColour())
                ):
                    if (
                            (gameGrid[i + 1][j] == None or gameGrid[i + 1][j].get_tokenColour() ==
                             game.getPlayers()[0].get_playerColour()) and
                            (gameGrid[i + 1][j - 2] == None or gameGrid[i + 1][j - 2].get_tokenColour() ==
                             game.getPlayers()[0].get_playerColour())
                    ):
                        numberOfWinningConfigurations += 1

            # bottom left
            if (2 <= i <= 9 and 0 <= j <= 9):
                if (
                        (gameGrid[i - 2][j] == None or gameGrid[i - 2][j].get_tokenColour() ==
                         game.getPlayers()[0].get_playerColour()) and
                        (gameGrid[i][j + 2] == None or gameGrid[i][j + 2].get_tokenColour() ==
                         game.getPlayers()[0].get_playerColour()) and
                        (gameGrid[i - 1][j + 1] == None or gameGrid[i - 1][j + 1].get_tokenColour() ==
                         game.getPlayers()[0].get_playerColour()) and
                        (gameGrid[i - 2][j + 2] == None or gameGrid[i - 2][j + 2].get_tokenColour() ==
                         game.getPlayers()[0].get_playerColour())
                ):
                    if (
                            (gameGrid[i - 1][j] == None or gameGrid[i - 1][j].get_tokenColour() ==
                             game.getPlayers()[0].get_playerColour()) and
                            (gameGrid[i - 1][j + 2] == None or gameGrid[i - 1][j + 2].get_tokenColour() ==
                             game.getPlayers()[0].get_playerColour())
                    ):
                        numberOfWinningConfigurations += 1

            # bottom right
            if (2 <= i <= 9 and 2 <= j <= 11):
                if (
                        (gameGrid[i - 2][j] == None or gameGrid[i - 2][j].get_tokenColour() ==
                         game.getPlayers()[0].get_playerColour()) and
                        (gameGrid[i - 1][j - 1] == None or gameGrid[i - 1][j - 1].get_tokenColour() ==
                         game.getPlayers()[0].get_playerColour()) and
                        (gameGrid[i][j - 2] == None or gameGrid[i][j - 2].get_tokenColour() ==
                         game.getPlayers()[0].get_playerColour()) and
                        (gameGrid[i - 2][j - 2] == None or gameGrid[i - 2][j - 2].get_tokenColour() ==
                         game.getPlayers()[0].get_playerColour())
                ):
                    if (
                            (gameGrid[i - 1][j] == None or gameGrid[i - 1][j].get_tokenColour() ==
                             game.getPlayers()[0].get_playerColour()) and
                            (gameGrid[i - 1][j - 2] == None or gameGrid[i - 1][j - 2].get_tokenColour() ==
                             game.getPlayers()[0].get_playerColour())
                    ):
                        numberOfWinningConfigurations += 1

            return numberOfWinningConfigurations


        y = searchPosition[0]
        x = searchPosition[1]
        maxList = []
        """
        if game.getGameGrid()[y][x] is None:
            maxScore = searchScore(game, searchPosition)
            maxList.append(searchPosition)
        else:
        """
        maxScore = 0

        #if (0 <= y-maxDepth <= 9 and 0 <= x-maxDepth <= 11) and (0 <= y+maxDepth <= 9 and 0 <= x+maxDepth <= 11):
        for i in range(y-maxDepth, y+(maxDepth+1)):
            for j in range(x-maxDepth, x+(maxDepth+1)):
                if game.getGameGrid()[i][j] is not None:
                    continue
                if (0 <= i <= 9 and 0 <= j <= 11):
                    if searchScore(game, [i, j]) > maxScore:
                        maxScore = searchScore(game, [i, j])
                        for element in maxList:
                            maxList.pop()
                        maxList.append([i,j])
                    elif searchScore(game, [i, j]) == maxScore:
                        maxList.append([i, j])

        return maxList


    def minimax(game, currentMove, depth, maximizingPlayer, origin):
        if depth == 0:
            return Heuristic.searchScore1(game, currentMove)

        if maximizingPlayer:

            childScore, best_childScore = Node.Node(0,[]), 0
            for y in range(origin[0] - 2, origin[0] + 3):
                for x in range(origin[1] - 2, origin[1] + 3):
                    if game.getGameGrid()[y][x] is None:
                        nextMove = [y,x]
                        game.getPlayers()[0].placeToken(game, game.getPlayers()[0].get_playerTokens(), nextMove)
                        childScore.set_score(max(childScore.get_score(), Heuristic.minimax(game, nextMove, depth - 1, False, origin)))

                        if best_childScore != childScore.get_score():
                            childScore.set_position(nextMove)
                            best_childScore = childScore.get_score()

                        print(childScore.get_score(), childScore.get_position(), best_childScore, "max")

                        game.getPlayers()[0].get_playerTokens().append(game.getGameGrid()[y][x])
                        game.getGameGrid()[y][x] = None

            return childScore

        else:
            childScore, worst_childScore = Node.Node(1000,[]), 1000
            for y in range(origin[0] - 2, origin[0] + 3):
                for x in range(origin[1] - 2, origin[1] + 3):
                    if game.getGameGrid()[y][x] is None:
                        nextMove = [y,x]
                        game.getPlayers()[1].placeToken(game, game.getPlayers()[1].get_playerTokens(), nextMove)
                        childScore.set_score(min(childScore.get_score(), Heuristic.minimax(game, nextMove, depth - 1, True, origin)))

                        if worst_childScore != childScore.get_score():
                            childScore.set_position(nextMove)
                            worst_childScore = childScore.get_score()

                        print(childScore.get_score(), childScore.get_position(), worst_childScore, "min")

                        game.getPlayers()[1].get_playerTokens().append(game.getGameGrid()[y][x])
                        game.getGameGrid()[y][x] = None

            return childScore.get_score()

    #-------------------------------------------------------------------------------------------------------------------


    def searchScore1(game, searchPosition):
        """
        Method to get the score of each individual search positions

        game                The game that is being played on
        searchPosition      The current grid position being evaluated
        """
        y = searchPosition[0]
        x = searchPosition[1]

        """score1 = 0.2 * (15 - game.getPlayers()[0].get_nbTokens())
        score2 = -0.1 * (15 - game.getPlayers()[1].get_nbTokens())
        score3 = 0
        score4 = 0"""
        score5 = Heuristic.getNumberOfWinningConfigurations1(game, searchPosition)

        """for i in range(y - 1, y + 2):
            for j in range(x - 1, x + 2):
                if (0 <= i <= 9 and 0 <= j <= 11) and (game.getGameGrid()[i][j] is not None):
                    if game.getGameGrid()[i][j].get_tokenColour() == game.getPlayers()[0].get_playerColour():
                        score3 += 1
                    else:
                        score4 += 1

        score3 *= 0.2
        score4 *= -0.1"""

        return score5

    def getNumberOfWinningConfigurations1(game, searchPosition):
        """
            Returns the number of winning configurations for the searchPosition.
            This is determined by determining how many of the 5 winning possible winning configurations can be generated (Center, TL, TR, BL, BR)
            if the token was placed at that position

            searchPosition : Current gameGrid position being evaluated for its position.
            game : The game that is being played on

        """
        i = searchPosition[1]
        j = searchPosition[0]
        gameGrid = game.getGameGrid()
        AiPlayer = game.getPlayers()[0]
        centerPieces, topleftPieces, toprightPieces, bottomleftPieces, bottomrightPieces = 0, 0, 0, 0, 0


        # Center
        if (1 <= i <= 8 and 1 <= j <= 10):
            if (
                    (gameGrid[i + 1][j + 1] is None or gameGrid[i + 1][j + 1].get_tokenColour() ==
                     AiPlayer.get_playerColour()) and
                    (gameGrid[i + 1][j - 1] is None or gameGrid[i + 1][j - 1].get_tokenColour() ==
                     AiPlayer.get_playerColour()) and
                    (gameGrid[i - 1][j + 1] is None or gameGrid[i - 1][j + 1].get_tokenColour() ==
                     AiPlayer.get_playerColour()) and
                    (gameGrid[i - 1][j - 1] is None or gameGrid[i - 1][j - 1].get_tokenColour() ==
                     AiPlayer.get_playerColour())
            ):
                if gameGrid[i + 1][j + 1] is not None:
                    centerPieces += 1
                if gameGrid[i + 1][j - 1] is not None:
                    centerPieces += 1
                if gameGrid[i - 1][j + 1] is not None:
                    centerPieces += 1
                if gameGrid[i - 1][j - 1] is not None:
                    centerPieces += 1


        # top left
        if (0 <= i <= 7 and 0 <= j <= 9):
            if (
                    (gameGrid[i][j + 2] is None or gameGrid[i][j + 2].get_tokenColour() ==
                     AiPlayer.get_playerColour()) and
                    (gameGrid[i + 1][j + 1] is None or gameGrid[i + 1][j + 1].get_tokenColour() ==
                     AiPlayer.get_playerColour()) and
                    (gameGrid[i + 2][j] is None or gameGrid[i + 2][j].get_tokenColour() ==
                     AiPlayer.get_playerColour()) and
                    (gameGrid[i + 2][j + 2] is None or gameGrid[i + 2][j + 2].get_tokenColour() ==
                     AiPlayer.get_playerColour())
            ):
                if gameGrid[i][j + 2] is not None:
                    topleftPieces += 1
                if gameGrid[i + 1][j + 1] is not None:
                    topleftPieces += 1
                if gameGrid[i + 2][j] is not None:
                    topleftPieces += 1
                if gameGrid[i + 2][j + 2] is not None:
                    topleftPieces += 1


        # top right
        if (0 <= i <= 7 and 2 <= j <= 11):
            if (
                    (gameGrid[i][j - 2] is None or gameGrid[i][j - 2].get_tokenColour() ==
                     AiPlayer.get_playerColour()) and
                    (gameGrid[i + 1][j - 1] is None or gameGrid[i + 1][j - 1].get_tokenColour() ==
                     AiPlayer.get_playerColour()) and
                    (gameGrid[i + 2][j] is None or gameGrid[i + 2][j].get_tokenColour() ==
                     AiPlayer.get_playerColour()) and
                    (gameGrid[i + 2][j - 2] is None or gameGrid[i + 2][j - 2].get_tokenColour() ==
                     AiPlayer.get_playerColour())
            ):
                if gameGrid[i][j - 2] is not None:
                    toprightPieces += 1
                if gameGrid[i + 1][j - 1] is not None:
                    toprightPieces += 1
                if gameGrid[i + 2][j] is not None:
                    toprightPieces += 1
                if gameGrid[i + 2][j - 2] is not None:
                    toprightPieces += 1


        # bottom left
        if (2 <= i <= 9 and 0 <= j <= 9):
            if (
                    (gameGrid[i - 2][j] is None or gameGrid[i - 2][j].get_tokenColour() ==
                     AiPlayer.get_playerColour()) and
                    (gameGrid[i][j + 2] is None or gameGrid[i][j + 2].get_tokenColour() ==
                     AiPlayer.get_playerColour()) and
                    (gameGrid[i - 1][j + 1] is None or gameGrid[i - 1][j + 1].get_tokenColour() ==
                     AiPlayer.get_playerColour()) and
                    (gameGrid[i - 2][j + 2] is None or gameGrid[i - 2][j + 2].get_tokenColour() ==
                     AiPlayer.get_playerColour())
            ):
                if gameGrid[i - 2][j] is not None:
                    bottomleftPieces += 1
                if gameGrid[i][j + 2] is not None:
                    bottomleftPieces += 1
                if gameGrid[i - 1][j + 1] is not None:
                    bottomleftPieces += 1
                if gameGrid[i - 2][j + 2] is not None:
                    bottomleftPieces += 1

        # bottom right
        if (2 <= i <= 9 and 2 <= j <= 11):
            if (
                    (gameGrid[i - 2][j] is None or gameGrid[i - 2][j].get_tokenColour() ==
                     AiPlayer.get_playerColour()) and
                    (gameGrid[i - 1][j - 1] is None or gameGrid[i - 1][j - 1].get_tokenColour() ==
                     AiPlayer.get_playerColour()) and
                    (gameGrid[i][j - 2] is None or gameGrid[i][j - 2].get_tokenColour() ==
                     AiPlayer.get_playerColour()) and
                    (gameGrid[i - 2][j - 2] is None or gameGrid[i - 2][j - 2].get_tokenColour() ==
                     AiPlayer.get_playerColour())
            ):
                if gameGrid[i - 2][j] is not None:
                    bottomrightPieces += 1
                if gameGrid[i - 1][j - 1] is not None:
                    bottomrightPieces += 1
                if gameGrid[i][j - 2] is not None:
                    bottomrightPieces += 1
                if gameGrid[i - 2][j - 2] is not None:
                    bottomrightPieces += 1

        return max(centerPieces, topleftPieces, toprightPieces, bottomleftPieces, bottomrightPieces)
