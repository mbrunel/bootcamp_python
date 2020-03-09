import sys

i = -1

if (len(sys.argv) != 2):
	exit()
arg = sys.argv[1]
if arg.isnumeric() == False:
	print("ERROR")
elif int(arg) == 0:
	print("I'm Zero.")
elif int(arg) % 2 == 0:
	print("I'm Even.")
elif int(arg) % 2 == 1:
	print("I'm Odd.")
else:
	print("ERROR")