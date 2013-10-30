import math

# Keskmine
def keskmine(numbers): # numbers on massiiv

	total = sum(numbers) / len(numbers)
	
	print (total)
	
# Fibonacci jada
def fibo(max):

	numbers = [0,1]
	
	for x in range(0, max):
		next = numbers[-1]+numbers[-2]
		numbers.append(next)
		
	print (numbers)

# Ruutvorrand
def equation(a, b, c):

	x1 = b**2 - 4 * a * c
			
	if x1 >= 0:
		x1 = math.sqrt(x1)
		x1 = -b + x1
		x1 = x1 / (2*a)
	else:
		x1 = 'unavailable'

	x2 = b**2 - 4 * a * c
	if x2 >= 0: 
		x2 = math.sqrt(x2)
		x2 = -b - x2
		x2 = x2 / (2*a)
	else:
		x2 = 'unavailable'

	print ("X1 is {} and X2 is {}".format(x1, x2))

keskmine([12,43,32,11])
fibo(100)
equation(-1,-2,3)
