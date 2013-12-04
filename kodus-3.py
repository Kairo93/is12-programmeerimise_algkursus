import math

height = 20
width = 50

y = 0

while y < height:

	sin = math.sin(y)

	display = int(round(sin*(width/2)))

	if sin > 0:
		display = display * '#'
		display = display.ljust(int(round(width/2)))
		display = display.rjust(width)

	else:
		display = -display * '#'
		display = display.rjust(int(round(width/2)))

	y += 0.1

	print display
