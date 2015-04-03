class piece:
	text_value = 'X'
	posX = 0
	posY = 0
	team = -1
	blocked_by_pieces = True
	blocked_by_attacks = False

	def __init__(self, posX, posY, team, text):
		self.posX = posX
		self.posY = posY
		self.team = team
		self.text_value = text

	def to_string(self):
		return self.text_value

	def can_move(self, x, y):
		print 'Checking if this piece can move like that'
		return False