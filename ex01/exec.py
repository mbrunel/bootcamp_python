import sys

i = 0
final = ''
stop = len(sys.argv) - 2

for arg in reversed(sys.argv):
	for car in reversed(arg):
		if car.islower():
			car = car.upper()
		elif car.isupper():
			car = car.lower()
		final = ''.join([final, car])
	if i == stop:
		break
	final = ''.join([final, ' '])
	i += 1
print(final)