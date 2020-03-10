# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    filterwords.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbrunel <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/10 04:09:23 by mbrunel           #+#    #+#              #
#    Updated: 2020/03/10 05:10:03 by mbrunel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def error():
	print("ERROR")
	exit()

test = True
loop = True
i = 0

try:
	try:
		test = int(sys.argv[1])
		test = False
	except:
		string = str(sys.argv[1]).split()
		length = int(sys.argv[2])
except:
	error()
if test == False:
	error()

while (loop == True):
	try:
		if len(string[i]) < length:
			del string[i]
		else:
			i += 1
	except:
		loop = False
print(string)
