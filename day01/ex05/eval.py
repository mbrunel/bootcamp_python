# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    eval.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbrunel <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/12 03:42:39 by mbrunel           #+#    #+#              #
#    Updated: 2020/03/12 04:04:53 by mbrunel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from functools import reduce

class Evaluator:
	def zip_evaluate(coefs, words):
		try:
			zipped = zip(coefs, words)
		except:
			return -1
		tot = 0
		for e in zipped:
			tot += e[0] * len(e[1])
		return tot
