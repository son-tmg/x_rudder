import Game, Player, Token, node, copy,time

class Heuristic:
    """The heuristic object contains the minimax function for a game grid"""

    def __init__(self, game_node):
        self._game_node = node.node(game_node)     #node containing the game object

    def get_game_node(self):
        return self._game_node


    def utility(self,node):
        """Calculates the utility of the state

            node : node containing game object
        """
        utility = 0
        utility = 3*self.getNumberOfWinningConfigurations1(node)
        #utility = 4*self.feature1(node) -2*self.feature2(node) + 

        return utility

    def getNumberOfWinningConfigurations1(self, node):
        """
            Returns the number of winning configurations for the searchPosition.
            This is determined by determining how many of the 5 winning possible winning configurations can be generated (Center, TL, TR, BL, BR)
            if the token was placed at that position

            searchPosition : Current gameGrid position being evaluated for its position.
            game : The game that is being played on

        """

        game = node.get_element()
        searchPosition = node.get_next_move()


        gameGrid = game.getGameGrid()
        AiPlayer = game.getPlayers()[0]
        centerPieces, topleftPieces, toprightPieces, bottomleftPieces, bottomrightPieces = 0, 0, 0, 0, 0

        #find all of the max tokens
        max_tokens = []

        for row in range(7,10):
            for column in range(0,3):
                if node.get_element().getGameGrid()[row][column] is not None:
                    token = game.getGameGrid()[row][column]
                    if token.get_tokenColour() == AiPlayer.get_playerColour():
                        max_tokens.append(token)

        for token in max_tokens:
            i = token.get_tokenPosition()[0]
            j = token.get_tokenPosition()[1]

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




    def feature1(self,node):
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
        state = node.get_element()

        total_number_of_movements_left_to_win_as_center = 0
        max_token_colour = state.getPlayers()[0].get_playerColour()

        max_tokens = []

        for row in range(7,10):
            for column in range(0,3):
                if state.getGameGrid()[row][column] is not None:
                    token = state.getGameGrid()[row][column]
                    if token.get_tokenColour() == max_token_colour:
                        max_tokens.append(token)

        for token in max_tokens:
            tokens_left_to_win_as_center = 0
            i = token.get_tokenPosition()[0]
            j = token.get_tokenPosition()[1]

            corners = []    #the 4 corners adjacent to center
            TL = [i-1,j-1]  #Top left
            TR = [i-1,j+1]  #Top right
            BL = [i+1,j-1]  #bottom left
            BR = [i+1,j+1]  #bottom right

            if TL[0] in range(7,10) and TL[1] in range(0,3):
                corners.append(TL)
            if TR[0] in range(7,10) and TR[1] in range(0,3):
                corners.append(TR)
            if BL[0] in range(7,10) and BL[1] in range(0,3):
                corners.append(BL)
            if BR[0] in range(7,10) and BR[1] in range(0,3):
                corners.append(BR)                

            # for each of the corners, check if they have the same colour as max_token_colour
            for corner in corners:

                row = corner[0]
                column = corner[1]
                if state.getGameGrid()[row][column] is not None:
                    token = state.getGameGrid()[row][column]
                    if token.get_tokenColour() == max_token_colour:
                        total_number_of_movements_left_to_win_as_center += 1
                
        return total_number_of_movements_left_to_win_as_center
                            

    def feature2(self,node):
        """
        opponent tokens to the left and right to block center token of max"""

        """
            find how many min tokens are to the left and right of all possible max center tokens
        """
        state = node.get_element()

        opponent_tokens_to_the_left_and_right = 0
        max_token_colour = state.getPlayers()[0].get_playerColour()
        min_token_colour = state.getPlayers()[1].get_playerColour()

        max_token = []

        #find all centered max tokens
        for row in range(7,10):
            for column in range(0,3):
                if state.getGameGrid()[row][column] is not None:
                    token = state.getGameGrid()[row][column]
                    if token.get_tokenColour() == max_token_colour:
                        max_token.append(token)

        #foreach of the max token, if that token was center, how many min tokens are to its left and right ?
        
        blocking_left_tokens = 0 #number of left side tokens
        blocking_right_tokens = 0  #number of right side tokens
        
        for token in max_token:
            i = token.get_tokenPosition()[1]
            j = token.get_tokenPosition()[0]
 

            left = [i,j-1]  # left
            right = [i,j+1]  # right
            
            # for the left and ride sides, check if they have the same colour as max_token_colour
            
            if (left[1] in range(0,3)):
                if state.getGameGrid()[left[0]][left[1]] is not None: 
                    left_token = state.getGameGrid()[left[0]][left[1]]
                    if token.get_tokenColour() != min_token_colour:
                        blocking_left_tokens += 1

            if (right[1] in range(0,3)):
                if state.getGameGrid()[right[0]][right[1]] is not None:
                    right_token = state.getGameGrid()[right[0]][right[1]]
                    if token.get_tokenColour() != min_token_colour:
                        blocking_right_tokens += 1

        opponent_tokens_to_the_left_and_right = blocking_left_tokens + blocking_right_tokens

        return opponent_tokens_to_the_left_and_right


    def feature3(self,node):
        """number of possible win paths containing 2 diagonals"""
        

    def generate_game_states(self,root_node,maximizing_player, depth):
        """Generate new game states by placing or moving tokens to up to a certain depth.
        
            root_node :     a node containing a game object
            maximizing_player :     boolean which tells if player is max or not
            depth : depth at which to search children for
         """

        root = root_node            #root node for which to generate children
        possible_placements = []    #list containing list of possible token positions
        possible_movements = []     #list containing list of possible token movements
        
        #generate all possible positions where a token can be placed or moved to.
        for row in range(7,10):
            for column in range(0,3):
                if root.get_element().getGameGrid()[row][column] is None:
                    possible_placements.append([row,column])
                else :
                    possible_movements.append([row,column])

        #depth 1 : generate all children by moving token to that position
        if maximizing_player:
            for placement in possible_placements:
                child_node = copy.deepcopy(root.get_element())    #copy of original game state object
                child_node.getPlayers()[0].placeToken(child_node , child_node.getPlayers()[0].get_playerTokens() , placement)
                new_node = node.node(child_node)
                new_node.set_next_move(placement)
                root.add_to_list_of_children(new_node)
                
            
            for movement in possible_movements:
                """
                    generate all possible movements of distance 1 to None positions : TOP, TL, TR, B , BL , BR
                    generate all game states with for each possible movement
                    add them to the list of children to root.
                """

            if depth == 2:
                for children in root.get_list_of_children():
                    self.generate_game_states(children,False,0)    
                
        else:
            for placement in possible_placements:
                child_node = copy.deepcopy(root.get_element())    #copy of original game state object
                child_node.getPlayers()[1].placeToken(child_node , child_node.getPlayers()[1].get_playerTokens() , placement)
                new_node = node.node(child_node)
                new_node.set_next_move(placement)
                root.add_to_list_of_children(new_node)

            for movement in possible_movements:
                """
                    generate all possible movements of distance 1 to None positions
                    generate all game states with for each possible movement
                    add them to the list of children to root.
                """

            if depth == 2:
                for children in root.get_list_of_children():
                    self.generate_game_states(children,True,0)         


    def alphabeta(self,node,depth, alpha, beta, maximizing_player):
        """minimax algorithm
        
           node : node containing the game object
           depth : depth of minimax search
           alpha : alpha cutoff
           beta : beta cutoff
           maximizing player : max player

           returns the node with the best heuristic value and game object containing the next best position
        """

        """
            if depth == 0 :
                return self.utility(node)
            if maximizing_player:
                v = f;pat('-inf')
                for child in node.get_list_of_children():
                    v_child = self.alphabeta(child.get_utility_score(),depth-1,alpha,beta,False)
                    if v_child > v :
                        next_node = v_child
                    v = max(v,v_child)
                    if beta <= alpha:
                        break
                return (v,child)
        
        """

        if depth == 0:
            return self.utility(node)

        if maximizing_player:
            v = float('-inf')   #worst case for max
            for child in node.get_list_of_children():
                v_child = self.alphabeta(child,depth-1,alpha,beta,False)
                child.set_utility_score(v_child)
                v = max(v,v_child)
                alpha = max(alpha,v)
                if beta <= alpha:
                    break
            return v
        else :
            v = float('inf')    #worst case for min
            for child in node.get_list_of_children():
                v_child = self.alphabeta(child,depth-1,alpha,beta,True)
                child.set_utility_score(v_child)
                v = min(v,v_child)
                beta = min(beta,v)
                if beta <= alpha:
                    break
            return v

    def find_next_move(self):
        """finds next move for Game grid by calling alphabeta on the game node"""

        self.generate_game_states(self.get_game_node(),True,2)
        heuristic_score = heuristic.alphabeta(self.get_game_node(),2,neg_inf,inf,True)
 
        print("The next node will have a heuristic of :", heuristic_score)
        print("from the following children: ")

        for child in self.get_game_node().get_list_of_children():
            if child.get_utility_score() == heuristic_score:
                next_node = child

        row = child.get_next_move()[0]
        col = child.get_next_move()[1]

        new_token = Token.Token("\u2588   ", [row,col])
        print("The next move is : " , child.get_next_move())
        self.get_game_node().get_element().getGameGrid()[row][col] = new_token

        print("The new game grid with new token:")
        self.get_game_node().get_element().printGameGrid()

if __name__ == "__main__":

    player1 = Player.Player("Sonam", "\u2588   ")
    player2 = Player.Player("Sonam", "\u2591   ")
    player1.InitializeTokenList()
    player2.InitializeTokenList()
    list_of_players = [player1,player2]

    new_game = Game.Game(list_of_players)
    # print(new_game.printGameGrid())

    heuristic = Heuristic(new_game)

    # start = time.time()
    # heuristic.generate_game_states(heuristic.get_game_node(),True,2)
    # end = time.time()
    # print("It took ", end - start , "seconds to generate nodes till depth 2.")
    
    # print(heuristic.feature1(heuristic.get_game_node().get_element(),True))

    inf = float('inf')
    neg_inf = float('-inf')

    # child_node = heuristic.alphabeta(heuristic.get_game_node(),2,neg_inf,inf,True)    
    # heuristic.get_game_node().set_next_move(child_node[1].get_next_move())

    # print(child_node[1].get_next_move())

    white_token = Token.Token("\u2588   ",[8,1])
    black_token = Token.Token("\u2591   ",[8,2])



    new_game_grid = [ 
					[None,None,None,None,None,None,None,None,None,None,None,None],
					[None,None,None,None,None,None,None,None,None,None,None,None],
					[None,None,None,None,None,None,None,None,None,None,None,None],
					[None,None,None,None,None,None,None,None,None,None,None,None],
					[None,None,None,None,None,None,None,None,None,None,None,None],
					[None,None,None,None,None,None,None,None,None,None,None,None],
					[None,None,None,None,None,None,None,None,None,None,None,None],
					[None,None,None,None,None,None,None,None,None,None,None,None],
					[None,white_token,black_token,None,None,None,None,None,None,None,None,None],
					[None,None,None,None,None,None,None,None,None,None,None,None],
			]
    
    heuristic.get_game_node().get_element().setGameGrid(new_game_grid)

    for i in range(0,2):
        heuristic.find_next_move()
