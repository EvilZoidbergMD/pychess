class space:
	occupied = False
	occupant = None
	string_value = ' '

	def __init__(self, text):
		self.string_value = text

	def to_string(self):
		if self.occupied:
			return self.occupant.to_string()
		else:
			return self.string_value

	def set_occupant(self, p):
		self.occupied = True
		self.occupant = p

	def clear_occupant(self):
		self.occupied = False
		self.occupant = None