import pygame
from pygame import gfxdraw
import math
import random


pygame.init()

size = width, height = 600, 800
margin = math.floor(width * .05) # 5% width of screen
bg_color = 20, 20, 20
white = (220, 220, 220)

screen = pygame.display.set_mode(size)

# line length and thickness
length = width - (2 * margin)
thickness = 10
# gap between lines
gap = int(length / 3)
# radius of circle
r = int((gap-30)/2)	


def draw_grid(): # 3x3 grid

	# determine line coordinates
	v1 = margin + gap
	v2 = margin + gap*2

	# draw lines - vertical
	pygame.draw.line(screen, white, \
		(v1, margin), (v1, margin+length), thickness)
	pygame.draw.line(screen, white, \
		(v2, margin), (v2, margin+length), thickness)

	# draw lines - horizontal
	pygame.draw.line(screen, white, \
		(margin, v1), (margin+length, v1), thickness)
	pygame.draw.line(screen, white, \
		(margin, v2), (margin+length, v2), thickness)


def draw_x(x, y): # (x, y) is the center of the circle
	r_ = r - 30 # for adjusting the size
	thickness_ = thickness + 8 # for adjusting the thickness
	x1 = [x-r_, x+r_]# start x: [first, second line]
	y1 = y - r_	   # end y
	x2 = [x+r_, x-r_]# end x: [first, second line]
	y2 = y + r_ 	   # end y 
	pygame.draw.line(screen, white, (x1[0],y1), (x2[0],y2), thickness_)
	pygame.draw.line(screen, white, (x1[1],y1), (x2[1],y2), thickness_)
def draw_o(x, y): # (x, y) is the center of the circle
	# anti-aliased circle
	r_ = r - 20 # for adjusting the radius
	thickness_ = thickness + 4 # for adjusting the thickness
	pygame.gfxdraw.aacircle(screen, int(x),int(y), \
		r_, white)
	pygame.gfxdraw.filled_circle(screen, int(x),int(y), \
		r_, white)
	pygame.gfxdraw.aacircle(screen, int(x),int(y), \
		r_-thickness_, bg_color)
	pygame.gfxdraw.filled_circle(screen, int(x),int(y), \
		r_-thickness_, bg_color)
	# non-anti-aliased circle
	# pygame.draw.circle(screen, white, \
	# (x, y), r_, thickness_)


def place(info):
	# loop 
		# wait until clicked
		# if clicked on valid spot:
			# mouse_pos = get mouse pos
			# shape_pos = pos(mouse_pos) ############################# pos() function is to be added
			# draw_x(shape_pos)
			# put shape location in info list
			# end loop
	pass


def horizontal(info, index, winner): # horizontal scan
	# for i in index
		# line = [index-1, index, index+1]
		# if all in line = O or X
			# winner = O or X
	pass
def vertical(info, index, winner):
	# for i in index
		# line = [index-3, index, index+3]
		# if all in line = O or X
			# winner = O or X	
	pass # vertical scan
def diagonal(info, index, winner):
	# for i in index
		# line1 = [index-4, index, index+4]
		# line2 = [index-2, index, index+2]
		# if all in line1 = O or X or 
			# winner = O or X
		# if all in line2 = O or X
			# winner = O or X
	pass # diagonal scan
def check_outcome(info):
	# indices of board:
	# 0 1 2 
	# 3 4 5
	# 6 7 8

	# winner = -1
	# scan board(8 scans total)
		# 1, 7: horizontal scan(2 scans)
			# horizontal(info, (1, 7), winner)
		# 3, 5: vertical scan(2 scans)
			# vertical(info, (3, 5), winner)
		# 4: horizontal and vertical scan, two diagonal scans(4 scans)
			# horizontal(info, (4), winner)
			# vertical(info, (4), winner)
			# diagonal(info, (4), winner)
	# return winner
	pass


def play():
	# determine who goes first
	# first = random.randint(0, 1)
	# info = empty list
	# loop starts with who goes first
		# place(info) / computer_place?(info)
		# check_outcome(info)
		# if player win: add player score
		# if computer win: add computer score
		# end
	pass # start of game


def play_loop(): # play() loop
	# score starts off at 0
	# loop
		# wait for player click
		# play()
	pass


def main():
	clock = pygame.time.Clock()
	run = True
	while run:
		clock.tick(60)

		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				run = False
			if event.type == pygame.MOUSEBUTTONUP:
				pass

		screen.fill(bg_color)
		draw_o(300-gap,300-gap)
		draw_x(300+gap,300-gap)
		draw_grid()

		pygame.display.flip()

	pygame.quit()
	quit()


main()
