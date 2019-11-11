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
        utility = 5*self.feature1(node) -4*self.feature2(node)

        return utility



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

        for row in range(2,6):
            for column in range(4,8):
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
            corners.extend([TL,TR,BL,BR])

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
        for row in range(2,6):
            for column in range(4,8):
                if state.getGameGrid()[row][column] is not None:
                    token = state.getGameGrid()[row][column]
                    if token.get_tokenColour() == max_token_colour:
                        max_token.append(token)

        #foreach of the max token, if that token was center, how many min tokens are to its left and right ?
        
        for token in max_token:
            i = token.get_tokenPosition()[0]
            j = token.get_tokenPosition()[1]
 
            blocking_left_tokens = 0 #number of left side tokens
            blocking_right_tokens = 0  #number of right side tokens
            left = [i,j-1]  # left
            right = [i,j+1]  # right
            

            # for the left and ride sides, check if they have the same colour as max_token_colour
            

            if state.getGameGrid()[left[0]][left[1]] is not None:

                left_token = state.getGameGrid()[left[0]][left[1]]
                if token.get_tokenColour() != min_token_colour:
                     blocking_left_tokens += 1

            if state.getGameGrid()[right[0]][right[1]] is not None:
                right_token = state.getGameGrid()[right[0]][right[1]]
                if token.get_tokenColour() != min_token_colour:
                    blocking_right_tokens += 1

        opponent_tokens_to_the_left_and_right = blocking_left_tokens + blocking_right_tokens

        return opponent_tokens_to_the_left_and_right


    def feature3(self):
        """"""


    def generate_game_states(self,root_node,maximizing_player, depth):
        """Generate new game states by placing or moving tokens to up to a certain depth
        
            node :     a node containing a game object
         """

        root = root_node
        possible_placements = []    #list containing list of possible token positions
        possible_movements = []     #list containing list of possible token movements
        

        for row in range(2,6):
            for column in range(4,8):
                if root.get_element().getGameGrid()[row][column] is None:
                    possible_placements.append([row,column])
                else :
                    possible_movements.append([row,column])

        #depth 1

        if maximizing_player:
            
            for placement in possible_placements:
                child_node = copy.deepcopy(root.get_element())    #copy of original game state object
                child_node.getPlayers()[0].placeToken(child_node , child_node.getPlayers()[0].get_playerTokens() , placement)
                new_node = node.node(child_node)
                root.add_to_list_of_children(new_node)
            
            if depth == 2:
                for children in root.get_list_of_children():
                    self.generate_game_states(children,False,0)    
                
        else:
            for placement in possible_placements:
                child_node = copy.deepcopy(root.get_element())    #copy of original game state object
                child_node.getPlayers()[1].placeToken(child_node , child_node.getPlayers()[1].get_playerTokens() , placement)

                new_node = node.node(child_node)
                root.add_to_list_of_children(new_node)

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
        """

        if depth == 0:
            return self.utility(node)

        if maximizing_player:
            v = float('-inf')
            for child in node.get_list_of_children():
                v = max([v,self.alphabeta(child,depth - 1,alpha, beta, False )])
                alpha = max([alpha,v])
                if beta <= alpha:
                    break
            return v
        else :
            v = float('inf')
            for child in node.get_list_of_children():
                v = min([v,self.alphabeta(child,depth - 1, alpha, beta,False )])
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



    start = time.time()
    heuristic.generate_game_states(heuristic.get_game_node(),True,2)
    end = time.time()
    print("It took ", end - start , "seconds to generate nodes till depth 2.")
    
    # print(heuristic.feature1(heuristic.get_game_node().get_element(),True))

    inf = float('inf')
    neg_inf = float('-inf')

    returned = heuristic.alphabeta(heuristic.get_game_node(),2,neg_inf,inf,True)

    print(returned)













