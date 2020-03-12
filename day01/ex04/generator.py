# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbrunel <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/12 02:58:30 by mbrunel           #+#    #+#              #
#    Updated: 2020/03/12 03:28:42 by mbrunel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

def generator(text, sep=" ", option=None):
	'''Option is an optional arg, sep is mandatory'''
	if (type(text) != str or (option != None and option != "ordered" and option != "shuffle")):
		yield "ERROR"
		return

	l = text.split(sep)
	if option == "ordered":
		l.sort()
	if option == "shuffle":
		random.shuffle(l)
	
	for word in l:
		yield word
