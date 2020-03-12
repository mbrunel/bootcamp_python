# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    logger.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbrunel <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/12 06:07:22 by mbrunel           #+#    #+#              #
#    Updated: 2020/03/12 06:50:55 by mbrunel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time
from random import randint

def log(func):
	f = open("machine.log", "a")
	name = str(func).split()[1].split('.')[1].split('_')
	f.write(name[0] + " " + name[1] +  "\n")
	def inner1(*args, **kwargs):
		return func(*args, **kwargs)
	return inner1

class CoffeeMachine():

	water_level = 100

	@log
	def start_machine(self):
		if self.water_level > 20:
			return True
		else:
			print("Please add water!")
		return False
	
	@log
	def boil_water(self):
		return "boiling..."

	@log
	def make_coffee(self):
		if self.start_machine():
			for _ in range(20):
				time.sleep(0.05)
				self.water_level -= 1
			print(self.boil_water())
			print("Coffee is ready!")

	@log
	def add_water(self, water_level):
		time.sleep(randint(1, 2))
		self.water_level += water_level
		print("Blub blub blub...")


if __name__ == "__main__":
	machine = CoffeeMachine()
	for i in range(0, 5):
		machine.make_coffee()

		machine.make_coffee()
		machine.add_water(70)
