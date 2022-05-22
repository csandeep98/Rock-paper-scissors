from pickle import NONE
import random
import math


class Player:
    def __init__(self, letter):
        # letter is either x or 0
        self.letter = letter

    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    # get a random spot from the available places

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = NONE
        while not valid_square:
            square = input(
                self.letter + '\',s turn, input number between {0,9} : ')
            # now we will apply constraints to the input and get the required values
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError

            except ValueError:
                print('invalid input, please try again ')

        return val
