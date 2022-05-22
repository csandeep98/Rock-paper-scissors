
from Player import HumanPlayer, RandomComputerPlayer


class TicTacToe:
    def __init__(self):
        # using single list to keep track of 3x3 matrix
        self.board = ['' for _ in range(9)]
        self.current_winner = None  # to keep track of the winner

    def print_board(self):

        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| '+' |'.join(row)+' |')  # this just gets the rows

    @staticmethod  # using this we need not call the class during execution
    # static is independent of the class and is concerned about the parameters passed to it
    def print_board_nums():
        # 0 | 1 | 2 tells us which number is located in what box
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]
                        for j in range(3)]

        for row in number_board:
            print('| '+' |'.join(row)+' |')

    # now we need to check the available spaces

    def available_moves(self):
        moves = []
        for (i, post) in enumerate(self.board):
            if post == ' ':
                moves.append(i)
        return moves

    def get_empty(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        # if it is a valid move then assign the letter to the board
        # then return True if valid else return False
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # in the game the winner will have 3 consecutive letters
        #horizontally, vertically, diagonally
        # lets check rows first
        row_index = square//3
        row = self.board[row_index*3:(row_index+1)*3]
        if all([spot == letter for spot in row]):
            return True

        col_index = square % 3
        col = [self.board[col_index + (i*3)] for i in range(3)]
        if all([spot == letter for spot in col]):
            return True

        # check diagonals
        # for diagonals the only possible indices are [0,4,6,8]
        # ie they are all even
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 6]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'  # this is the starting letter

    while game.get_empty():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        # now we need to define a function to make a move
        if game.make_move(square, letter):
            if print_game:
                print(letter+f' makes a move to square {square}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + 'wins')
                return letter

            # after the move is made we need to alternate letters
            if letter == 'X':
                letter = 'O'
            else:
                letter = 'X'
        if print_game:
            print('its a tie')


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
