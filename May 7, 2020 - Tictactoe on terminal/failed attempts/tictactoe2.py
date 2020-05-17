import os


class Board:

	def __init__(self):
		self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

	def draw(self):
		print(" %s | %s | %s " %(self.cells[1], self.cells[2], self.cells[3]))
		print("-----------")
		print(" %s | %s | %s " %(self.cells[4], self.cells[5], self.cells[6]))
		print("-----------")
		print(" %s | %s | %s " %(self.cells[7], self.cells[8], self.cells[9]))

	def update(self, cell_no, player):
		if self.cells[cell_no] == " ":
			self.cells[cell_no] = player

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

	def is_tie(self):
		used_cells = 0
		for cell in self.cells:
			if cell != " ":
				used_cells += 1
		if used_cells == 9:
			return True
		else:
			return False

	def reset(self):
		self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

	def play_again(player, self):
		if player != "":
			self.update(cell, player)
			print(f"{player} won")
		else:
			print("It's a tie")
		print("Play again? (Y/N)")
		play_again = input(">>>").upper()
		if play_again == "Y":
			self.reset()
		else:
			quit()


def print_header():
	print("Tic-Tac-Toe\n")
def clear():
	os.system('cls')
def refresh_screen():
	clear()
	print_header()
	board.draw()



board = Board()
while True:

	
	refresh_screen()
	print("\nX) Enter a cell number between 1-9")
	cell = int(input(">>>"))
	board.update(cell, "X")
	winner = board.check_win("X")
	if winner:
		board.play_again("X")

	refresh_screen()
	print("\nO) Enter a cell number between 1-9")
	cell = int(input(">>>"))
	board.update(cell, "O")
	board.check_win("O")
	winner = board.check_win("O")
	if winner:
		board.play_again("O")
	
	tie = board.is_tie()
	if tie:
		board.play_again("")
