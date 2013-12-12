def box(width, height):
	
	display = '#' * width + '\n'
	
	display += ('#' + ' ' * (width-2) + '#\n') * (height-2)

	display += '#' * width

	print display

box(10, 5)
