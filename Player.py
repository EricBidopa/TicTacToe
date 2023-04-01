import math
import random

class Player:
    def __init__(self, letter):
        #letter is x or o
        self.letter = letter
        #all players should get their next move.
    def get_move(self, game):
        pass 
    #useinheritance to build a ramdom computer player and a human computer player on top of the above class.
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    def get_move(self, game):
            #get random valid spot
        square = random.choice(game.available_moves())
        return square
        
class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')
                #to check if this a correct value by trying to cast it to an integer and if it's not, then it is invalid.
                #if that spot is not available on the board, then it is also invalid.
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again')
        return val