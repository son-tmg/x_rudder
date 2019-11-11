import Game,Player

class node:

    def __init__(self, element):
        self._element = element
        self._list_of_children = []

    def get_element(self):
        return self._element
    
    def get_list_of_children(self):
        return self._list_of_children

    def set_element(self,element):
        self._element = element

    def add_to_list_of_children(self,child):
        #adds child to the end of the list of children
        self._list_of_children.append(child)


if __name__ == "__main__":

    player1 = Player.Player("Sonam","Black")
    player2 = Player.Player("Sashank",'White')
    players= []

    players.append(player1)
    players.append(player2)
    print(players)

    newGame = Game.Game(players)
    newNode = node(newGame)
    print(newNode)