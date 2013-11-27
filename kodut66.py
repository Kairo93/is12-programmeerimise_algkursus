import math

# Numbrikontroll
number1 = raw_input('Sisesta I number: ')
number2 = raw_input('Sisesta II number: ')

number1 = int(number1)
number2 = int(number2)

i = 0
total = abs(number1-number2)
answer = 0

while i <= total:
	i = i + 1

	if i % 3 == 0:
		answer = answer + 1

print 'Arvuvahemikul '+str(number1)+' - '+str(number2)+' on '+str(answer)+' 3-ga jaguvat arvu'

# Numbriotsingu abimees
def find_numbers(source):
	response = 0

	for i in source:
		if i.isdigit():
			response = 1
			break

	return response

# Stringikontroll
sisestus = raw_input('Sisestage tekst: ')

if find_numbers(sisestus) and sisestus.islower():
	print 'Sisestuses v2iksed t2hed ja numbrid'
elif not find_numbers(sisestus) and sisestus.islower():
	print 'Sisestuses v2iksed t2hed ja numbriteta'
elif find_numbers(sisestus) and sisestus.isupper():
	print 'Sisestuses suured t2hed ja numbrid'
elif not find_numbers(sisestus) and sisestus.isupper():
	print 'Sisestuses suured t2hed ja numbriteta'
else:
	if find_numbers(sisestus):
		print 'Sisestuses suured ja v2iksed t2hed ning numbrid'
	else:
		print 'Sisestuses suured ja v2iksed t2hed ja numbriteta'
