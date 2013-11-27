import math
import re

# Numbrikontroll
arv1 = raw_input('Sisestage I arv: ')
arv2 = raw_input('Sisestage II arv: ')

arv1 = int(arv1)
arv2 = int(arv2)

x = arv1
y = arv2

if x > y:
	x = arv2
	y = arv1

answer = 0

while x-1 < y:
	x = x + 1

	if x % 3 == 0:
		answer = answer + 1

print 'Vahemikus ('+str(arv1)+'-'+str(arv2)+') on 3-ga jagunevaid arve: '+str(answer)	

# Stringikontroll
sisestus = raw_input('Sisestage tekst: ')

if re.search(r'\d+', sisestus) and sisestus.islower():
	print 'Sisestuses v2iksed t2hed ja numbrid'
elif not re.search(r'\d+', sisestus) and sisestus.islower():
	print 'Sisestuses v2iksed t2hed ja numbriteta'
elif re.search(r'\d+', sisestus) and sisestus.isupper():
	print 'Sisestuses suured t2hed ja numbrid'
elif not re.search(r'\d+', sisestus) and sisestus.isupper():
	print 'Sisestuses suured t2hed ja numbriteta'
else:
	if re.search(r'\d+', sisestus):
		print 'Sisestuses suured ja v2iksed t2hed ja numbrid'
	else:
		print 'Sisestuses suured ja v2iksed t2hed ja numbriteta'
