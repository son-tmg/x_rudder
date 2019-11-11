import Game, Player, Token, node, math, copy,time

class Heuristic:
    """The heuristic object contains the minimax function for a game grid"""

    def __init__(self, state):
        self._state = state
        self._utility_score = 0

    def utility(self,state):
        """Calculates the utility of the state"""
        utility = 0
        utility = 5*feature1(state) - 4*feature2(state)

        return utility
    
    def feature1(self,state,maximizing_player):
        """total number of movements left to win as a center
        
            state : state of a game.

            return : total number of movements left to win as a center
        """

        """
            total_number_of_movements_to_win_as_center = 0
            for each token:
                compute number of movements left to win as a center
    
            return total_number_of_movements_left_to_win_as_center
        """

        total_number_of_movements_left_to_win_as_center = 0
        max_token_colour = state.getPlayers()[0].get_tokenColour()

        max_tokens = []

        for row in range(2,8):
            for column in range(2,10):
                if state.getGameGrid()[row][column] is not None:
                    token = state.getGameGrid()[row][column]
                    if token.get_tokenColour == max_token_colour:
                        max_tokens.apend(token)

        for token in max_tokens:
            tokens_left_to_win_as_center = 0
            i = token.get_tokenPosition()[0]
            j = token.get_tokenPosition()[1]

            corners = []    #the 4 corners adjacent to center
            TL = [i-1,j-1]  #Top left
            TR = [i-1,j+1]  #Top right
            BL = [i+1,j-1]  #bottom left
            BR = [i+1,j+1]  #bottom right
            corners.extend(TL,TR,BL,BR)

            # for each of the corners, check if they have the same colour as max_token_colour
            for corner in corners:

                row = corner[0]
                column = corner[1]
                if state.getGameGrid()[row][column] is not None:
                    token = state.getGameGrid()[row][column]
                    if token.get_tokenColour() == max_token_colour:
                        total_number_of_movements_left_to_win_as_center += 1
                
            return total_number_of_movements_left_to_win_as_center
                            

    def feature2(self,state):
        """opponent tokens to the left and right to block center token of max"""

        """
            find how many min tokens are to the left and right of all possible max center tokens
        """
        opponent_tokens_to_the_left_and_right = 0
        max_token_colour = state.getPlayers()[0].get_tokenColour()
        min_token_colour = state.getPlayers()[1].get_tokenColour

        max_token = []

        #find all centered max tokens
        for row in range(2,8):
            for column in range(2,10):
                if state.getGameGrid()[row][column] is not None:
                    token = state.getGameGrid()[row][column]
                    if token.get_tokenColour == max_token_colour:
                        max_token.apend(token)

        #foreach of the max token, if that token was center, how many min tokens are to its left and right ?
        
        for token in max_token:
            i = token.get_tokenPosition()[0]
            j = token.get_tokenPosition()[1]
 
            blocking_left_tokens = 0 #number of left side tokens
            blocking_right_tokens = 0  #number of right side tokens
            left = [i,j-1]  # left
            right = [i,j+1]  # right

            # for each of the corners, check if they have the same colour as max_token_colour
            

            if state.getGameGrid()[left[0]][left[1]] is not None:
                left_token = state.getGameGrid()[left[0]][left[1]]
                if token.get_tokenColour() == min_token_colour:
                     blocking_left_tokens += 1

                right_token = state.getGameGrid()[right[0]][right[1]]
                if token.get_tokenColour() == min_token_colour:
                    blocking_right_tokens += 1

        opponent_tokens_to_the_left_and_right = blocking_left_tokens + blocking_right_tokens

        return opponent_tokens_to_the_left_and_right

    def feature3(self):
        """"""

    def generate_game_states(self,state,maximizing_player):
        """Generate new game states by placing or moving tokens to up to a certain depth
        
            state :     a game object
         """

        possible_placements = []    #list containing list of possible token positions
        possible_movements = []     #list containing list of possible token movements
        possible_states = []
        

        for row in range(2,8):
            for column in range(2,10):
                if state.getGameGrid()[row][column] is None:
                    possible_placements.append([row,column])
                else :
                    possible_movements.append([row,column])

        if maximizing_player:
            for placement in possible_placements:
                state_copy = copy.deepcopy(state)    #copy of original state
                state_copy.getPlayers()[0].placeToken(state_copy , state_copy.getPlayers()[0].get_playerTokens() , placement)
                possible_states.append(state_copy)
        else:
            for placement in possible_placements:
                state_copy = copy.deepcopy(state)    #copy of original state
                state_copy.getPlayers()[1].placeToken(state_copy , state_copy.getPlayers()[1].get_playerTokens() , placement)
                possible_states.append(state_copy)

        return possible_states


    def alphabeta(self,node,depth, alpha, beta, maximizing_player):
        """minimax algorithm
        
           node : node containing the game grid
           depth : depth of minimax search
           alpha : alpha cutoff
           beta : beta cutoff
           maximizing player : max player

        """

        if depth == 0 or node.checkState():
            return self.utility(node)

        if maximizing_player:
            v = -math.inf
            for child in node.get_list_of_children:
                v = max([v,self.minimax(child,depth - 1, False )])
                alpha = max([alpha,v])
                if beta <= alpha:
                    break
            return v
        else :
            v = math.inf
            for child in node.get_list_of_children:
                v = min([v,self.minimax(child,depth - 1, False )])
                beta = min([beta,v])
                if beta <= alpha:
                    break
            return v



if __name__ == "__main__":

    player1 = Player.Player("Sonam", "\u2588  ")
    player2 = Player.Player("Sonam", "\u2591   ")
    player1.InitializeTokenList()
    player2.InitializeTokenList()
    list_of_players = [player1,player2]

    new_game = Game.Game(list_of_players)
    # print(new_game.printGameGrid())

    heuristic = Heuristic(new_game)
    children = heuristic.generate_game_states(new_game,True)


    #depth 1

    start = time.time()

    root = node.node(new_game)
    for child in children:
        root.add_to_list_of_children(node.node(child))

    end = time.time()
    print("It took ", end - start , "seconds to generate  : " ,len(root.get_list_of_children()), " children of root.")


    #depth 2

    start = time.time()

    number_of_game_states = 0

    for child_node in root.get_list_of_children():
        children2 = heuristic.generate_game_states(child_node.get_element(),False)
        
        for child in children2:
            child_node.add_to_list_of_children(child)

        number_of_game_states += len(child_node.get_list_of_children())

    end = time.time()
    print("It took ", end - start , "seconds to generate " ,number_of_game_states, " children for each children of root ")







    # @staticmethod
    # def searchList(game, searchPosition, maxDepth = 1):
    #     """
    #     Method to get the list of positions to check, returning the positions which have the highest evaluation

    #     game                The game that is being played on
    #     searchPosition      The current grid position being evaluated, with its specified perimeter positions
    #     maxDepth            The maximum perimeter depth the function will look into to find the score
    #     """

    #     def searchScore(game, searchPosition):
    #         """
    #         Method to get the score of each individual search positions

    #         game                The game that is being played on
    #         searchPosition      The current grid position being evaluated
    #         """
    #         y = searchPosition[0]
    #         x = searchPosition[1]
    #         score1 = 0.2 * (15 - game.getPlayers()[0].get_nbTokens())
    #         score2 = -0.1 * (15 - game.getPlayers()[1].get_nbTokens())
    #         score3 = 0
    #         score4 = 0
    #         score5 = 0.4 * getNumberOfWinningConfigurations(searchPosition, game)

    #         for i in range(y - 1, y + 2):
    #             for j in range(x - 1, x + 2):
    #                 if (0 <= i <= 9 and 0 <= j <= 11) and (game.getGameGrid()[i][j] is not None):
    #                     if game.getGameGrid()[i][j].get_tokenColour() == game.getPlayers()[0].get_playerColour():
    #                         score3 += 1
    #                     else:
    #                         score4 += 1

    #         score3 *= 0.2
    #         score4 *= -0.1

    #         # Addition of score5 from heuristic feature 5 * weight of function 5
    #         return (score1 + score2 + score3 + score4 + score5)

    #     def getNumberOfWinningConfigurations(searchPosition, game):
    #         """
    #             Returns the number of winning configurations for the searchPosition.
    #             This is determined by determining how many of the 5 winning possible winning configurations can be generated (Center, TL, TR, BL, BR)
    #             if the token was placed at that position

    #             searchPosition : Current gameGrid position being evaluated for its position.
    #             game : The game that is being played on

    #         """
    #         numberOfWinningConfigurations = 0
    #         gameGrid = game.getGameGrid()
    #         i = searchPosition[1]
    #         j = searchPosition[0]

    #         # Center
    #         if (1 <= i <= 8 and 1 <= j <= 10):
    #             if (
    #                     (gameGrid[i + 1][j + 1] == None or gameGrid[i + 1][j + 1].get_tokenColour() ==
    #                      game.getPlayers()[0].get_playerColour()) and
    #                     (gameGrid[i + 1][j - 1] == None or gameGrid[i + 1][j - 1].get_tokenColour() ==
    #                      game.getPlayers()[0].get_playerColour()) and
    #                     (gameGrid[i - 1][j + 1] == None or gameGrid[i - 1][j + 1].get_tokenColour() ==
    #                      game.getPlayers()[0].get_playerColour()) and
    #                     (gameGrid[i - 1][j - 1] == None or gameGrid[i - 1][j - 1].get_tokenColour() ==
    #                      game.getPlayers()[0].get_playerColour())
    #             ):
    #                 if (
    #                         (gameGrid[i][j - 1] == None or gameGrid[i][j - 1].get_tokenColour() ==
    #                          game.getPlayers()[0].get_playerColour()) and
    #                         (gameGrid[i][j + 1] == None or gameGrid[i][j + 1].get_tokenColour() ==
    #                          game.getPlayers()[0].get_playerColour())

    #                 ):
    #                     numberOfWinningConfigurations += 1

    #         # top left
    #         if (0 <= i <= 7 and 0 <= j <= 9):
    #             if (
    #                     (gameGrid[i][j + 2] == None or gameGrid[i][j + 2].get_tokenColour() ==
    #                      game.getPlayers()[0].get_playerColour()) and
    #                     (gameGrid[i + 1][j + 1] == None or gameGrid[i + 1][j + 1].get_tokenColour() ==
    #                      game.getPlayers()[0].get_playerColour()) and
    #                     (gameGrid[i + 2][j] == None or gameGrid[i + 2][j].get_tokenColour() ==
    #                      game.getPlayers()[0].get_playerColour()) and
    #                     (gameGrid[i + 2][j + 2] == None or gameGrid[i + 2][j + 2].get_tokenColour() ==
    #                      game.getPlayers()[0].get_playerColour())
    #             ):
    #                 if (
    #                         (gameGrid[i + 1][j] == None or gameGrid[i + 1][j].get_tokenColour() ==
    #                          game.getPlayers()[0].get_playerColour()) and
    #                         (gameGrid[i + 1][j + 2] == None or gameGrid[i + 1][j + 2].get_tokenColour() ==
    #                          game.getPlayers()[0].get_playerColour())
    #                 ):
    #                     numberOfWinningConfigurations += 1

    #         # top right
    #         if (0 <= i <= 7 and 2 <= j <= 11):
    #             if (
    #                     (gameGrid[i][j - 2] == None or gameGrid[i][j - 2].get_tokenColour() ==
    #                      game.getPlayers()[0].get_playerColour()) and
    #                     (gameGrid[i + 1][j - 1] == None or gameGrid[i + 1][j - 1].get_tokenColour() ==
    #                      game.getPlayers()[0].get_playerColour()) and
    #                     (gameGrid[i + 2][j - 2] == None or gameGrid[i + 2][j - 2].get_tokenColour() ==
    #                      game.getPlayers()[0].get_playerColour()) and
    #                     (gameGrid[i + 2][j] == None or gameGrid[i + 2][j].get_tokenColour() ==
    #                      game.getPlayers()[0].get_playerColour())
    #             ):
    #                 if (
    #                         (gameGrid[i + 1][j] == None or gameGrid[i + 1][j].get_tokenColour() ==
    #                          game.getPlayers()[0].get_playerColour()) and
    #                         (gameGrid[i + 1][j - 2] == None or gameGrid[i + 1][j - 2].get_tokenColour() ==
    #                          game.getPlayers()[0].get_playerColour())
    #                 ):
    #                     numberOfWinningConfigurations += 1

    #         # bottom left
    #         if (2 <= i <= 9 and 0 <= j <= 9):
    #             if (
    #                     (gameGrid[i - 2][j] == None or gameGrid[i - 2][j].get_tokenColour() ==
    #                      game.getPlayers()[0].get_playerColour()) and
    #                     (gameGrid[i][j + 2] == None or gameGrid[i][j + 2].get_tokenColour() ==
    #                      game.getPlayers()[0].get_playerColour()) and
    #                     (gameGrid[i - 1][j + 1] == None or gameGrid[i - 1][j + 1].get_tokenColour() ==
    #                      game.getPlayers()[0].get_playerColour()) and
    #                     (gameGrid[i - 2][j + 2] == None or gameGrid[i - 2][j + 2].get_tokenColour() ==
    #                      game.getPlayers()[0].get_playerColour())
    #             ):
    #                 if (
    #                         (gameGrid[i - 1][j] == None or gameGrid[i - 1][j].get_tokenColour() ==
    #                          game.getPlayers()[0].get_playerColour()) and
    #                         (gameGrid[i - 1][j + 2] == None or gameGrid[i - 1][j + 2].get_tokenColour() ==
    #                          game.getPlayers()[0].get_playerColour())
    #                 ):
    #                     numberOfWinningConfigurations += 1

    #         # bottom right
    #         if (2 <= i <= 9 and 2 <= j <= 11):
    #             if (
    #                     (gameGrid[i - 2][j] == None or gameGrid[i - 2][j].get_tokenColour() ==
    #                      game.getPlayers()[0].get_playerColour()) and
    #                     (gameGrid[i - 1][j - 1] == None or gameGrid[i - 1][j - 1].get_tokenColour() ==
    #                      game.getPlayers()[0].get_playerColour()) and
    #                     (gameGrid[i][j - 2] == None or gameGrid[i][j - 2].get_tokenColour() ==
    #                      game.getPlayers()[0].get_playerColour()) and
    #                     (gameGrid[i - 2][j - 2] == None or gameGrid[i - 2][j - 2].get_tokenColour() ==
    #                      game.getPlayers()[0].get_playerColour())
    #             ):
    #                 if (
    #                         (gameGrid[i - 1][j] == None or gameGrid[i - 1][j].get_tokenColour() ==
    #                          game.getPlayers()[0].get_playerColour()) and
    #                         (gameGrid[i - 1][j - 2] == None or gameGrid[i - 1][j - 2].get_tokenColour() ==
    #                          game.getPlayers()[0].get_playerColour())
    #                 ):
    #                     numberOfWinningConfigurations += 1

    #         return numberOfWinningConfigurations


    #     y = searchPosition[0]
    #     x = searchPosition[1]
    #     maxList = []
    #     """
    #     if game.getGameGrid()[y][x] is None:
    #         maxScore = searchScore(game, searchPosition)
    #         maxList.append(searchPosition)
    #     else:
    #     """
    #     maxScore = 0

    #     #if (0 <= y-maxDepth <= 9 and 0 <= x-maxDepth <= 11) and (0 <= y+maxDepth <= 9 and 0 <= x+maxDepth <= 11):
    #     for i in range(y-maxDepth, y+(maxDepth+1)):
    #         for j in range(x-maxDepth, x+(maxDepth+1)):
    #             if game.getGameGrid()[i][j] is not None:
    #                 continue
    #             if (0 <= i <= 9 and 0 <= j <= 11):
    #                 if searchScore(game, [i, j]) > maxScore:
    #                     maxScore = searchScore(game, [i, j])
    #                     for element in maxList:
    #                         maxList.pop()
    #                     maxList.append([i,j])
    #                 elif searchScore(game, [i, j]) == maxScore:
    #                     maxList.append([i, j])

    #     return maxList