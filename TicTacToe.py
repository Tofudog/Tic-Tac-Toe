#import numpy as np
#import random
import time

class Game:
	def __init__(self, rows, cols):
		self.nrows = rows
		self.ncols = cols
		self.board = [ ['_' for c in range(cols)] for r in range(rows) ]
		#self.board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	def turn(self, player):
		row = int(input(f"Player {player} choose a row (1-{self.nrows}): "))
		col = int(input(f"Player {player} choose a row (1-{self.nrows}): "))
		self.board[row-1][col-1] = player
	def over(self):
		return self.horizontal() or self.vertical() or self.diagonal()
	def horizontal(self):
		for row in range(self.nrows):
			check = self.board[row][0]
			same = True
			if check == '_':
				continue
			for col in range(1, self.ncols):
				if check != self.board[row][col]:
					same = False
			if same is True:
				return True
		return False
	def vertical(self):
		for col in range(self.ncols):
			check = self.board[0][col]
			same = True
			if check == '_':
				continue
			for row in range(1, self.nrows):
				if check != self.board[row][col]:
					same = False
			if same is True:
				return True
		return False
	def diagonal(self):
		check1 = self.board[0][0]
		same = True
		for row in range(1, self.nrows):
			#col must equal row
			if check1 != self.board[row][row]:
				same = False
		if same is True and check1 != '_':
			return True
		check2 = self.board[self.nrows-1][0]
		for row in range(1, self.nrows):
			#col must equal self.nrows-row-1
			if check2 != self.board[self.nrows-row-1][row]:
				return False
		return check2 != '_'
	def display(self):
		for row in self.board:
			print(row)

def main():
	R = int(input("Enter the number of rows: "))
	C = int(input("Enter the number of columns: "))
	p1 = input("Player 1 enter first initial: ")
	p2 = input("Player 2 enter first initial: ")
	game = Game(R, C)
	game.display()
	#time.sleep(1)
	while not game.over():
		game.turn(p1)
		game.display()
		#if game.over at this instant, then player 2 loses
		if game.over():
			print("Player 1 wins!")
			time.sleep(3)
			return 1
		game.turn(p2)
		game.display()
	print("Player 2 wins!")
	time.sleep(3)
	return 0

if __name__=='__main__':
	main()