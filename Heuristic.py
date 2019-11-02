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
        score4 = self.getNumberOfWinningConfigurations(self,searchPosition,game)

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



    def getNumberOfWinningConfigurations(self,searchPosition,game):
        """
            Returns the number of winning configurations for the searchPosition.
            This is determined by determining how many of the 5 winning possible winning configurations can be generated (Center, TL, TR, BL, BR)
            if the token was placed at that position

            searchPosition : Current gameGrid position being evaluated for its position.
            gameGrid : 

        """
        numberOfWinningConfigurations = 0
        gameGrid = game.getGameGrid()
        i = searchPosition[1]
        j = searchPosition[0]

        
		#Center
        if ( 1<=i<=8 and 1<=j<=10):
			if (
			    gameGrid[i+1][j+1] == None or gameGrid[i+1][j+1].get_tokenColour() == "\u2588   " and
				gameGrid[i+1][j-1] == None or gameGrid[i+1][j-1].get_tokenColour() == "\u2588   " and
				gameGrid[i-1][j+1] == None or gameGrid[i-1][j+1].get_tokenColour() ==  "\u2588   " and 
				gameGrid[i-1][j-1] == None or gameGrid[i-1][j-1].get_tokenColour() == "\u2588   "
			):
				if (
					gameGrid[i][j-1] == None or gameGrid[i][j-1].get_tokenColour() == "\u2588   "  or 
					gameGrid[i][j+1] == None or gameGrid[i][j+1].get_tokenColour() == "\u2588   "
					):
						numberOfWinningConfigurations += 1

        #top left						
        if ( 0<=i<=7 and 0<=j<=9 ):		
			if (
				gameGrid[i][j+2] == None or gameGrid[i][j+2].get_tokenColour() == "\u2588   " and
				gameGrid[i+1][j+1] == None or gameGrid[i+1][j+1].get_tokenColour() == "\u2588   " and
				gameGrid[i+2][j] == None or gameGrid[i+2][j].get_tokenColour() == "\u2588   " and 
				gameGrid[i+2][j+2] == None or gameGrid[i+2][j+2].get_tokenColour() == "\u2588   "
			):
				if (
					gameGrid[i+1][j] == None or gameGrid[i+1][j].get_tokenColour() == "\u2588   " or
					gameGrid[i+1][j+2] == None or gameGrid[i+1][j+2].get_tokenColour() == "\u2588   "
					):
					    numberOfWinningConfigurations += 1

		#top right
        if ( 0<=i<=7 and 2<=j<=11 ):	
            if (
                gameGrid[i][j-2] == None or gameGrid[i][j-2].get_tokenColour() == "\u2588   " and
                gameGrid[i+1][j-1] == None or gameGrid[i+1][j-1].get_tokenColour() == "\u2588   " and
                gameGrid[i+2][j-2] == None or gameGrid[i+2][j-2].get_tokenColour() == "\u2588   " and 
                gameGrid[i+2][j] == None or gameGrid[i+2][j].get_tokenColour() == "\u2588   "
            ):
                if (
                    gameGrid[i+1][j] == None or gameGrid[i+1][j].get_tokenColour() == "\u2588   " or
                    gameGrid[i+1][j-2] == None or gameGrid[i+1][j-2].get_tokenColour() == "\u2588   "
                    ):
                        numberOfWinningConfigurations += 1

        #bottom left
		if (2<=i<=9 and 0<=j<=9):
			if (
				gameGrid[i-2][j] == None or gameGrid[i-2][j].get_tokenColour() == "\u2588   " and
				gameGrid[i][j+2] == None or gameGrid[i][j+2].get_tokenColour() == "\u2588   " and
				gameGrid[i-1][j+1] == None or gameGrid[i-1][j+1].get_tokenColour() == "\u2588   " and 
				gameGrid[i-2][j+2] == None or gameGrid[i-2][j+2].get_tokenColour() == "\u2588   "
			):
				if (
					gameGrid[i-1][j] == None or gameGrid[i-1][j].get_tokenColour() == "\u2588   " or
					gameGrid[i-1][j+2] == None or gameGrid[i-1][j+2].get_tokenColour() == "\u2588   "
					):
						numberOfWinningConfigurations += 1

		#bottom right			
		if (2<=i<=9 and 2<=j<=11):		
			if (
				gameGrid[i-2][j] == None or gameGrid[i-2][j].get_tokenColour() == "\u2588   " and
				gameGrid[i-1][j-1] == None or gameGrid[i-1][j-1].get_tokenColour() == "\u2588   " and
				gameGrid[i][j-2] == None or gameGrid[i][j-2].get_tokenColour() == "\u2588   " and 
				gameGrid[i-2][j-2] == None or gameGrid[i-2][j-2].get_tokenColour() == "\u2588   "
			):
				if (
					gameGrid[i-1][j] == None or gameGrid[i-1][j].get_tokenColour() == "\u2588   " or
					gameGrid[i-1][j-2] == None or gameGrid[i-1][j-2].get_tokenColour() == "\u2588   "
					):
						numberOfWinningConfigurations += 1

        return numberOfWinningConfigurations