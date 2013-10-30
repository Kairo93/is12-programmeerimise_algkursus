import time

global gx
global gy

gx = 0
gy = 0

def elukas_print():

	print "\033[" + str(gy) + ";" + str(gx) + "H$"


def elukas_xy():
	print "{};{}".format(gx, gy)
	return [gx, gy]

for yes in range(0, 20):
	elukas_print()
	time.sleep(1)

	elukas_xy()

