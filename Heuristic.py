import Game, Player, Token, random, Node, copy

class Heuristic:
    """The heuristic function used for the AI"""

    @staticmethod
    def minimax(game, currentMove, depth, maximizingPlayer, origin):
        if depth == 0:
            return Heuristic.searchScore(game, currentMove)

        if maximizingPlayer:

            childScoreMax, best_childScore = Node.Node(0,[]), 0
            for y in range(origin[0] - 4, origin[0] + 5):
                for x in range(origin[1] - 4, origin[1] + 5):
                    if (0<=y<=9 and 0<=x<=11) and game.getGameGrid()[y][x] is None:
                        nextMove = [y,x]
                        game.getPlayers()[0].placeToken(game, game.getPlayers()[0].get_playerTokens(), nextMove)
                        if game.getgameFinished():
                            print("Player " + game.getPlayers()[0].get_playerName() + " won.")
                            exit(1)
                        childScoreMax.set_score(max(childScoreMax.get_score(), Heuristic.minimax(game, nextMove, depth - 1, False, origin)))

                        if best_childScore != childScoreMax.get_score():
                            childScoreMax.set_position(nextMove)
                            best_childScore = childScoreMax.get_score()

                        print(childScoreMax.get_score(), childScoreMax.get_position(), best_childScore, "max")

                        game.getPlayers()[0].get_playerTokens().append(game.getGameGrid()[y][x])
                        game.getGameGrid()[y][x] = None

            return childScoreMax

        else:
            childScoreMin, worst_childScore = Node.Node(1000,[]), 1000
            for y in range(origin[0] - 2, origin[0] + 3):
                for x in range(origin[1] - 2, origin[1] + 3):
                    if game.getGameGrid()[y][x] is None:
                        nextMove = [y,x]
                        game.getPlayers()[1].placeToken(game, game.getPlayers()[1].get_playerTokens(), nextMove)
                        childScoreMin.set_score(min(childScoreMin.get_score(), Heuristic.minimax(game, nextMove, depth - 1, True, origin)))

                        if worst_childScore != childScoreMin.get_score():
                            childScoreMin.set_position(nextMove)
                            worst_childScore = childScoreMin.get_score()

                        print(childScoreMin.get_score(), childScoreMin.get_position(), worst_childScore, "min")

                        game.getPlayers()[1].get_playerTokens().append(game.getGameGrid()[y][x])
                        game.getGameGrid()[y][x] = None

            return childScoreMin.get_score()

    #-------------------------------------------------------------------------------------------------------------------


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
        score5 = Heuristic.getNumberOfWinningConfigurations(game, searchPosition)

        return (score1 + score2 + score5)

    def getNumberOfWinningConfigurations(game, searchPosition):
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
