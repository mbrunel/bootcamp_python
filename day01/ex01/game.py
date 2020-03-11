# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    game.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbrunel <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/11 07:59:00 by mbrunel           #+#    #+#              #
#    Updated: 2020/03/11 08:09:39 by mbrunel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GotCharacter:
	'''A GOT character'''

	def __init__(self, first_name, is_alive):
		self.first_name = first_name
		self.is_alive = is_alive

class Stark(GotCharacter):
	'''Someone from Stark'''
	def __init__(self, first_name=None, is_alive=True):
		super().__init__(first_name=first_name, is_alive=is_alive)
		self.family_name = "Stark"
		self.house_words = "Winter is Coming"
