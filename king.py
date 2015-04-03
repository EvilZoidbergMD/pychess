from settings import *
from piece import *

class king(piece):

	def __init__(self, posX, posY, team):
		text = 'X'
		if team == 0:
			text = white_pieces[5]
		else:
			text = black_pieces[5]
		piece.__init__(self, posX, posY, team, text)

		self.blocked_by_attacks = True

	def can_move(self, x, y):
		print 'Checking if this piece can move like that'
		return False