import sys

def text_analyzer(*strings):
	'''This function counts the number of upper characters, lower characters, punctuation and spaces in a given text.'''
	low = 0
	up  = 0
	punct = 0
	spaces = 0
	nbcar = 0

	if (len(strings) > 1):
		print("ERROR")
		return
	elif (len(strings) == 0):
		string = input("Enter your string here --->")
	else:
		string = strings[0]
	for c in string:
		nbcar += 1
		if c.islower():
			low += 1
		elif c.isupper():
			up += 1
		elif c == '.' or c == ',' or c == ';' or c == '?' or c == '!' or c == ':' or c == '\'' or c == '-' or c == '\"':
			punct += 1
		elif c == ' ' or c == '\t':
			spaces += 1
	print("nombre de minuscules : {0},\nnombre de majuscules : {1},\nnombre de separateurs : {2},\
		\nnombre d'espaces : {3},\nnombre totale de caracters : {4}".format(low, up, punct, spaces, nbcar))
	return
