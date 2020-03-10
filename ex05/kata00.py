# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata00.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbrunel <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/10 01:20:12 by mbrunel           #+#    #+#              #
#    Updated: 2020/03/10 02:14:59 by mbrunel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

t = (19, 42, 43, 67)
length = len(t)
if length == 0:
	exit()
print("the {0} numbers are:".format(length), end = ' ')
for arg in t:
	if arg != t[0]:
		print(",", end = ' ')
	print(arg, end = '')
	if arg != t[length - 1]:
		print(" ", end = '')
print("")
