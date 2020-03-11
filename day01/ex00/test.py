# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbrunel <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/10 23:59:37 by mbrunel           #+#    #+#              #
#    Updated: 2020/03/11 07:45:06 by mbrunel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from recipe import Recipe
from book import Book

recipe = Recipe("name", 3, 60, ["1", "2", "3"], "test", "dessert")
print(str(recipe))
book = Book("book", {"starter" : ["1", "2"], "lunch" : ["3", "4"], "dessert" : ["5", "6"]})
book.add_recipe(recipe)
print(book.last_update.year, book.creation_date.year)
print(str(book.get_recipe_by_name("5")))
print(str(book.get_recipes_by_type("dessert")))
