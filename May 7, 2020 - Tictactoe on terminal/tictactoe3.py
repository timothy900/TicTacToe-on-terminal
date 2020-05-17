'''
Finished on May 7, 2020
This is my 3rd attempt at making TicTacToe on terminal.
'''


import os
import random


class Board:

	# Added placeholder so index starts at 1, and not 0
	def __init__(self):
		self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
		self.scores = {"X":0, "O":0}

	def draw(self):
		print(" %s | %s | %s " %(self.cells[1], self.cells[2], self.cells[3]))
		print("-----------")
		print(" %s | %s | %s " %(self.cells[4], self.cells[5], self.cells[6]))
		print("-----------")
		print(" %s | %s | %s " %(self.cells[7], self.cells[8], self.cells[9]))

	def reset(self):
		self.cells = ["placeholder", " ", " ", " ", " ", " ", " ", " ", " ", " "]

	def update(self, cell_no, player):
		if self.cells[cell_no] == " ":
			self.cells[cell_no] = player

	def add_score(self, player):
		self.scores[player] += 1

	# Print the scores of players X and O
	def print_score(self):
		points = f'X: {self.scores["X"]} | O: {self.scores["O"]}'
		print(points, "\n")

	# Check all possible winning outcomes
	def check_win(self, player):
		c = self.cells

		if c[1]==player and c[2]==player and c[3]==player: 
			return True
		if c[4]==player and c[5]==player and c[6]==player: 
			return True
		if c[7]==player and c[8]==player and c[9]==player: 
			return True
		if c[1]==player and c[4]==player and c[7]==player: 
			return True
		if c[2]==player and c[5]==player and c[8]==player: 
			return True
		if c[3]==player and c[6]==player and c[9]==player: 
			return True
		if c[1]==player and c[5]==player and c[9]==player: 
			return True
		if c[3]==player and c[5]==player and c[7]==player: 
			return True
		else:
			return False

	# Check if there are any empty cells
	def check_full(self):
		if " " in self.cells:
			return False
		else:
			return True


# Initialize board
board = Board()

def print_header():
	print("\nTic-Tac-Toe\n")
def clear():
	os.system('cls')
def refresh_screen():
	clear()
	print_header()
	board.print_score()
	board.draw()

# Main loop
run = True
while run:
	# Reset board before starting
	board.reset()
	# Choose who goes first
	players = ["O", "X"]
	random.shuffle(players)
	# Start game
	play = True
	while play:
		refresh_screen()
		# Players take turns
		for player in players:
			# Ask for input
			while True:
				try:
					cell = int(input(f"{player}) Enter a cell between 1-9\n>>"))
					if 0 <= cell <= 9:
						break
				except ValueError:
					pass

			# Place input on board
			board.update(cell, player)
			# Check outcome
			win = board.check_win(player)
			full = board.check_full()
			# Refresh
			refresh_screen()
			# End play loop if won
			if win:
				board.add_score(player)
				refresh_screen()
				print(f"{player} won the game.")
				play = False
				break
			# End play loop if tied
			elif full and not win:
				refresh_screen()
				print("It was a tie.")
				play = False
				break


	# Ask if play again
	asking = True
	while asking:
		try:
			play_again = str(input("Play again?(Y/N)\n>>")).upper()
			# End asking loop if play again
			if play_again == "Y":
				asking = False
			# End run loop if not play again
			elif play_again == "N": 
				run = False
				break
		# If input is invalid
		except ValueError:
			pass

