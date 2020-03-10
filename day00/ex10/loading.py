# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    loading.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbrunel <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/10 06:41:08 by mbrunel           #+#    #+#              #
#    Updated: 2020/03/10 08:15:56 by mbrunel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from time import sleep
import time
import sys

def ft_progress(lst):
	total = len(lst)
	time_init = time.time()
	for i in range(total):
		progress = i / total + 0.000000000000001
		atm = time.time() - time_init
		if (i < 40):
			estim = 0
		else:
			estim = (atm / progress) - atm
		prog_bar = "[" + "=" * int((progress* 50)) + ">"
		str_prog = " [{:.0%}".format(progress) 
		string = "ETA:" + " {:>5.02f}s".format(estim) + str_prog + " " * (6 - len(str_prog)) + "]" + prog_bar + " " * (51 - len(prog_bar)) + "]"
		sys.stdout.write(string)
		sys.stdout.flush()
		sys.stdout.write("\b" * (len(string)))
		yield lst[i]

listy = range(1000)
ret = 0
for elem in ft_progress(listy):
	ret += (elem + 3) % 5
	sleep(0.01)
print()
print(ret)
