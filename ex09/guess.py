# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbrunel <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/10 06:20:43 by mbrunel           #+#    #+#              #
#    Updated: 2020/03/10 06:38:31 by mbrunel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy
from random import randint

print("This is an interactive guessing game!")
print("You have to enter a number between 1 and 99 to find out the secret number.")
print("Type 'exit' to end the game.")
print("Good luck!")
print("")

KeepRunning = True
tofind = randint(0, 99)
i = 0
while (KeepRunning == True):
	print("What's your guess between 1 and 99?")
	nb = input(">> ")
	if nb == "exit":
		print("bye")
		exit()
	try:
		nb = int(nb)
	except:
		print("That's not a number.")
		continue
	if nb < 0 or nb > 99:
		print("That's not a number between 1 and 99")
		continue
	if nb == tofind:
		print("Congratulations, you've got it")
		if i == 0:
			print("Congratulations! You got it on your first try!")
		else:
			print("You won in {0} attempts!".format(i))
		exit(0)
	elif nb < tofind:
		print("Too low!")
	else:
		print("Too high!")
	i += 1
