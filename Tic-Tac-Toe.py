import numpy as np
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

fill_value = "_"
game_board = np.full(shape=(3, 3), dtype=object, fill_value=fill_value)  # Init board and dtype=object to allow strings

# Accessing each value
# print(board[0, 0])  # Prints out first value
# print(board[0, 3])  # Gives error
# game_board[2, 1] = "x"  # Changes to x
# print(game_board)

class TicTacToe:
    """Init Variables needed:

    * board
    * Initials (e.g- x's and o's);
    * user_input-looped;
    """
    def __init__(self, board, first_initial, last_initial):
        self.board = board
        self.initial1 = first_initial
        self.initial2 = last_initial
        self.current_player = None
        self.winner = None

    def playerOneMoves(self):
        self.current_player = "Player One"
        row = int(input(f"Choose a row {self.current_player} (1-3): "))
        col = int(input(f"Choose a columns {self.current_player} (1-3): "))
        while True:
            if self.board[row-1, col-1] != fill_value:
                print((row, col), "is already taken up!")
                row = int(input(f"Choose a different row {self.current_player} (1-3): "))
                col = int(input(f"Choose a different column {self.current_player} (1-3): "))
            else:
                # Note that we must take row/col - 1 because of indexing
                self.board[row-1, col-1] = self.initial1
                break

    def playerTwoMoves(self):
        self.current_player = "Player Two"
        row = int(input(f"Choose a row {self.current_player} (1-3): "))
        col = int(input(f"Choose a columns {self.current_player} (1-3): "))
        while True:
            if self.board[row-1, col-1] != fill_value:
                print((row, col), "is already taken up!")
                row = int(input(f"Choose a different row {self.current_player} (1-3): "))
                col = int(input(f"Choose a different column {self.current_player} (1-3): "))
            else:
                self.board[row-1, col-1] = self.initial2
                break

    """Define functions to check if a player wins:
    
    Including:
    
    * Horizontal;
    * Vertical;
    * Diagonal;
    """
    def checkHorizontal(self):
        for row in range(len(self.board)):
            if self.board[row-1, 0] == self.initial1:
                if self.board[row-1, 0] == self.board[row-1, 1] == self.board[row-1, 2]:
                    self.winner = self.initial1
                    return True
            elif self.board[row-1, 0] == self.initial2:
                if self.board[row-1, 0] == self.board[row-1, 1] == self.board[row-1, 2]:
                    self.winner = self.initial2
                    return True

    def checkVertical(self):
        for col in range(len(self.board)):
            if self.board[0, col-1] == self.initial1:
                if self.board[0, col-1] == self.board[1, col-1] == self.board[2, col-1]:
                    self.winner = self.initial1
                    return True
            elif self.board[0, col-1] == self.initial2:
                if self.board[0, col-1] == self.board[1, col-1] == self.board[2, col-1]:
                    self.winner = self.initial1
                    return True

    def checkDiagonal(self):
        # To check diagonal:
        # Two possible variations;
        # Both special loops via functions
        if self.board[0, 0] == self.initial1:
            if self.loopDiagonalOne(self.board):
                self.winner = self.initial1
                return True

        elif self.board[0, 0] == self.initial2:
            if self.loopDiagonalOne(self.board):
                self.winner = self.initial2
                return True

        if self.board[0, 2] == self.initial1:
            if self.loopDiagonalTwo(self.board):
                self.winner = self.initial1
                return True

        elif self.board[0, 2] == self.initial2:
            if self.loopDiagonalTwo(self.board):
                self.winner = self.initial2
                return True

    def loopDiagonalOne(self, arr2D):
        return arr2D[0, 0] == arr2D[1, 1] == arr2D[2, 2]

    def loopDiagonalTwo(self, arr2D):
        return arr2D[0, 2] == arr2D[1, 1] == arr2D[2, 0]

    def gameDraw(self):
        if not (np.any(self.board == fill_value)):
            self.winner = "Draw"
            return True

    def gameOver(self):
        return self.checkHorizontal() or self.checkVertical() or self.checkDiagonal()

game = TicTacToe(game_board, "x", "o")

def tic_tac_toe():
    print(game.board)  # Prints initialized board
    while not game.gameOver():
        game.playerOneMoves()
        print(game.board)
        if not game.gameOver():
            """Reason for adding if statement:  
            In the event that player one wins,
            the game should immediately discontinue.
            However, without the if statement placed as such,
            player two moves and then it stops.
            """
            game.playerTwoMoves()
            print(game.board)
    print("Game Over")
    if game.winner != "Draw":
        print(game.winner, "wins!")
    else:
        print("It was a draw...")

tic_tac_toe()
