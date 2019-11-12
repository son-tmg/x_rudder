import Game,Player

class node:

    def __init__(self, element):
        self._element = element
        self._list_of_children = []
        self._next_move= None
        self._utility_score = None

    def get_element(self):
        return self._element
    
    def get_list_of_children(self):
        return self._list_of_children

    def get_next_move(self):
        return self._next_move

    def get_utility_score(self):
        return self._utility_score

    def set_next_move(self,next_move):
        self._next_move = next_move

    def set_element(self,element):
        self._element = element

    def set_utility_score(self,score):
        self._utility_score = score

    def add_to_list_of_children(self,child):
        #adds child to the end of the list of children
        self._list_of_children.append(child)

