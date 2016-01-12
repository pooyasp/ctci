import random 

class BlackJackHand:

	def __init__(self):
		self.cards = []

	def addCard(self, c):
		self.cards.append(c)

	def scores(self):
		score = [0]
		for c in self.cards:
			if c.rank < 10:
				if c.rank == 1:
					temp = []
					for s in score:
						temp.append(s + 1)
						temp.append(s + 11)
					score = temp
				else:
					for i in range(len(score)):
						score[i] += c.rank
			else:
				for i in range(len(score)):
					score[i] += 10
		return score

	def __str__(self):
		result = []
		for c in self.cards:
			result.append(str(c))

		return '\n'.join(result)


class DeckOfCards:
	def __init__(self):
		self.cards = []

		for i in range(1, 5):
			for j in range(1, 14):
				self.cards.append(Card(i, j))

	def shuffle(self):
		for i in range(len(self.cards)-1):
			j = random.randint(i+1, len(self.cards)-1)

			temp = self.cards[i]
			self.cards[i] = self.cards[j]
			self.cards[j] = temp

	def __str__(self):
		result = []

		for c in self.cards:
			result.append(str(c))

		return '\n'.join(result) 

	def deal(self):
		if self.cards == []:
			return None

		return self.cards.pop(0)

class Card:
	def __init__(self, face, rank):
		self.face = face
		self.rank = rank

	def __str__(self):
		return '[' + str(self.face) + ', ' + str(self.rank) + ']'




if __name__ == '__main__':
	d = DeckOfCards()
	d.shuffle()
	h = BlackJackHand()
	print(h)
	print('-------')
	
	h.addCard(d.deal())
	print(h)
	print(h.scores())
	print('-------')

	h.addCard(d.deal())
	print(h)
	print(h.scores())
	print('-------')

	h.addCard(d.deal())
	print(h)
	print(h.scores())
	print('-------')