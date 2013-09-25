import random
from random import randint

klass = ['kairo', 'jaanus', 'jeesus', 'patrick', 'spongebob', 'franco', 'aigar', 'timo']

print klass

#valik = random.choice(klass)
#print valik


index = randint(0, len(klass)-1)
print klass[index]
#del klass[2]
#print klass[index] 

print "\n"

kuulid = ["sinine"]*5 + ["must"]*10 + ["valge"]*15

kuul1 = randint(0, len(kuulid)-1)
del kuulid[kuul1]

kuul2 = randint(0, len(kuulid)-1)
del kuulid[kuul2]

print "Esimene kuul: %s Teine kuul: %s Kokku kuule nyyd: %i"% (kuulid[kuul1], kuulid[kuul2], len(kuulid))
