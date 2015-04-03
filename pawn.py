from settings import *
from piece import *

class pawn(piece):

	def __init__(self, posX, posY, team):
		text = 'X'
		if team == 0:
			text = white_pieces[0]
		else:
			text = black_pieces[0]
		piece.__init__(self, posX, posY, team, text)

	def can_move(self, x, y):
		print 'Checking if this piece can move like that'
		return False