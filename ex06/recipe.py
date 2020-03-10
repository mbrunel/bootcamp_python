# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    recipe.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbrunel <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/10 02:51:34 by mbrunel           #+#    #+#              #
#    Updated: 2020/03/10 04:07:07 by mbrunel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

cookbook = {"sandwich" : {"recipe" : ["ham", "bread", "cheese", "tomatoes"], "type" : "lunch", "duration" : 10},\
		"cake" : {"recipe" : ["flour", "sugar", "eggs"], "type" : "dessert", "duration" : 60},\
		"salad" : {"recipe" : ["avocado", "arugula", "tomatoes", "spinach"], "type" : "lunch", "duration" : 15}}

def print_cookbook():
	for e in cookbook:
		print(e)

def print_recipe(recipe):
	try:
		test = cookbook[recip]
	except:
		print("Enter a valid name")
		return
	print("Ingredients: ", end = '')
	for e in cookbook[recipe]["recipe"]:
		print(e, end = " ")
	print("")
	print("To eat at:", cookbook[recipe]["type"])
	print("Preparation time :", cookbook[recipe]["duration"])

def del_recipe(recipe):
	try:
		del cookbook[recipe]
	except:
		print("Enter a valid name")

def add_recipe(recipe, ingredients, typ, duration):
	cookbook[recipe] = {"recipe" : ingredients, "type" : typ, "duration" : duration}

running = True
print("Please select an option by typing the corresponding number:")
print("1: Add a recipe")
print("2: Delete a recipe")
print("3: Print a recipe")
print("4: Print the cookbook")
print("5: Quit")
print("")
while running == True:
	choice = input(">>")
	try:
		choice = int(choice)
	except:
		print("You must enter a digit between 1 and 5")
		continue
	if 1 <= choice <= 3:
		recipe = input("Enter a recipe name > ")
		if choice == 1:
			ingredients = input("enter the ingredients > ").split()
			typ = input("enter the typ > ")
			duration = input("enter the preparation time > ")
			add_recipe(recipe, ingredients, typ, duration)
		elif choice == 3:
			print_recipe(recipe)
		else:
			del_recipe(recipe)
	elif choice == 4:
		print_cookbook()
	elif choice == 5:
		print('Bye')
		exit()
	else:
		print("You must enter a digit between 1 and 5")
