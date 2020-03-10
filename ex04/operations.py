# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    operations.py                                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbrunel <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/10 00:22:58 by mbrunel           #+#    #+#              #
#    Updated: 2020/03/10 01:07:37 by mbrunel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def aff_error(error):
	if error == 1:
		print("InputError: too many argument\n")
	if error == 2:
		print("inputError: only number\n")
	print("Usage: python operations.py <number1> <number2>")
	print("Example:")
	print("\t python operations.py 10 3")
	exit()

if len(sys.argv) != 3:
	aff_error(1)
try:
	nb1 = int(sys.argv[1])
except:
	aff_error(2)
try:
	nb2 = int(sys.argv[2])
except:
	aff_error(2)
print("Sum:\t\t{0}".format(nb1 + nb2))
print("Difference:\t{0}".format(nb1 + nb2))
print("Product:\t{0}".format(nb1 * nb2))
try:
	print("Quotient:\t{0}".format(nb1 / nb2))
except:
	print("Quotient:\tERROR (div by zero)")
try:
	print("Remainder:\t{0}".format(nb1 % nb2))
except:
	print("Remainder:\tERROR·(div·by·zero)")
