import sys
from random import randint

def display(x, y, text):

	sys.stdout.write("\033[" + str(y) + ";" + str(x) + "H" + str(text))
	

def box(x, y, laius, korgus):

	display(x, y, '#' * laius)

	height = 0

	while height <= korgus:
		
		display(x, y + height, '#')
		display(x + laius, y + height, '#')
		
		height += 1

	display(x, y + korgus, '#' * laius)

	print

def stars(count):
	
	stars = 0
	star_positions = []
	
	while stars < count:
		
		x = randint(0, 70)
		y = randint(0, 20)

		display(x, y, '*')

		if [x, y] not in star_positions:
			star_positions.append([x, y])

			stars += 1

display(20, 12, 'Tekst')

box(16, 9, 11, 6)

stars(200)
