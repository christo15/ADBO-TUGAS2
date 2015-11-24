import Random

class Dice(object):
	def __init__(self):
		self._rnd = Random()

	def roll(self):
		return self._rnd.nextInt(6) + 1
