from settings import *
from piece import *

class knight(piece):

	def __init__(self, posX, posY, team):
		text = 'X'
		if team == 0:
			text = white_pieces[1]
		else:
			text = black_pieces[1]
		piece.__init__(self, posX, posY, team, text)

		self.blocked_by_pieces = False

	def can_move(self, x, y):
		print 'Checking if this piece can move like that'
		return False