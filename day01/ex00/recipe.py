# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbrunel <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/10 23:48:46 by mbrunel           #+#    #+#              #
#    Updated: 2020/03/11 07:45:00 by mbrunel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Recipe:
	def __init__(self, name, lvl, time, ingredients, description, typ):
		self.name = name
		self.lvl = lvl
		self.time = time
		self.ingredients = ingredients
		self.description = description
		self.type = typ
	def __str__(self):
		"""Return the string to print with the recipe info"""
		txt =f"""\
name :		{self.name}
lvl :		{self.lvl}
time :		{self.time}
ingredients :	{self.ingredients}
description :	{self.description}
type :		{self.type}\
"""
		return txt
