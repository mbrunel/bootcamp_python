# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    book.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbrunel <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/11 00:29:19 by mbrunel           #+#    #+#              #
#    Updated: 2020/03/11 07:44:59 by mbrunel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import datetime
from recipe import Recipe

class Book:
	def __init__(self, name, recipes_list):
		self.name = name
		self.last_update = datetime.datetime.now()
		self.creation_date = datetime.datetime.now()
		self.recipes_list = recipes_list

	def get_recipe_by_name(self, name):
		"""Print a recipe with the name `name` and return the instance"""
		if name in self.recipes_list.get("starter"):
			print(name)
			return "starter"
		elif name in self.recipes_list.get("dessert"):
			print(name)
			return "dessert"
		elif name in self.recipes_list.get("lunch"):
			print(name)
			return "lunch"
		else:
			print("No such recipe")
			return "ERROR"

	def get_recipes_by_type(self, typ):
		"""Get all recipe names for a given recipe_type """
		try:
			return self.recipes_list.get(typ)
		except:
			return "no such type"

	def add_recipe(self, recipe):
		"""Add a recipe to the book and update last_update"""
		try:
			new = Recipe(recipe.name, recipe.lvl, recipe.time, recipe.ingredients, recipe.description, recipe.type)
			self.recipes_list[new.type].append(new.name)
			self.last_update = datetime.datetime.now()
		except:
			print("not a recipe")
			return
