def visual(x, y):
	column = 0
	x -= 2

	# Columns loop
	while column < y:
		show = ''	

		hashes = 0
		dollars = 0
		
		# Add hashes
		while hashes <= (column):	
		
			show += '#'

			hashes += 1

		# Additional whitespace
		show += ' '

		# Add dollars
		while dollars <= (x - hashes):	
	
			show += '$'

			dollars += 1

		column += 1

		# Display
		print show

visual(7, 5)
