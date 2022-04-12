import math
import random

from numpy import less_equal

class Player:
    def __init__(self, letter):
        # letter can be x or o
        self.letter = letter

    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        
        square = random.choice(game.available_moves())
        return square

    

class HumanPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass

     