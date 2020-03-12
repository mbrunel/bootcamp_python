# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    generator.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbrunel <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/12 02:58:30 by mbrunel           #+#    #+#              #
#    Updated: 2020/03/12 03:17:39 by mbrunel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

def generator(text, sep=" ", option=None):
	'''Option is an optional arg, sep is mandatory'''
	l = text.split(sep)
	if option == "ordered":
		l.sort()
	if option == "shuffle":
		random.shuffle(l)
	for word in l:
		yield word
