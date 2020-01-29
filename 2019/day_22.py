from collections import deque

class Cards:
	def __init__(self, card):
		self.length = len(card)
		self.card = card
		self.deck = deque(card) # haha lol.. deck and deque??

	def getCard(self, number):
		for i in range(self.length):
			if self.card[i] == number:
				print(i)
				break

	def getPos(self, number):
		print(self.card[number])

	def viewDeck(self, N=0):
		if N == 0:
			N = self.length

		for i in range(N):
			print(self.card[i], end=" ")

		print()
	
	def deal(self):
		temp = deque()

		for i in range(self.length):
			x = self.deck.popleft()
			temp.appendleft(x)

		self.deck = temp
		self.card = list(temp)

	def cut(self, N):
		temp = deque()
		
		cut = self.card[:N]
		rest = self.card[N:][::-1]

		temp.extend(cut)
		temp.extendleft(rest)

		self.deck = temp
		self.card = list(temp)

	def increment(self, N):
		temp = [0 for i in range(self.length)]
		counter = 0
		pos = 0

		while pos != self.length:
			temp[counter] = self.card[pos]
			pos += 1
			counter = (counter + N) % self.length

		self.card = temp
		self.deck = deque(temp)

	
# main #
with open("day_22.txt") as f:
	instructions = [line.strip() for line in f.readlines()]

factoryDeck = [i for i in range(10007)]
game = Cards(factoryDeck)

for line in instructions:
	separate = line.split(" ")
	
	if separate[0] == "cut":
		game.cut(int(separate[-1]))
	else:
		if separate[1] == "with":
			game.increment(int(separate[-1]))
		else:
			game.deal()
	
game.getCard(2019)

