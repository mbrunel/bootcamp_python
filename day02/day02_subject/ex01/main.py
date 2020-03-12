# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbrunel <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/12 05:09:17 by mbrunel           #+#    #+#              #
#    Updated: 2020/03/12 06:01:12 by mbrunel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def what_are_the_vars(*args, **kwargs):
	"""Your code"""
	obj = getattr(ObjectC, "__init__")
	for e in dir(obj):
		if "__" in e:
			continue
		try:
			delattr(obj, e)
		except:
			continue
	i = 0
	for value in args:
		setattr(obj, "arg" + str(i), value)
		i += 1
	try:
		for key, value in kwargs.items():
			setattr(obj, key, value)
	except:
		pass
	return obj
class ObjectC(object):
	def __init__(self):
		pass

def doom_printer(obj):
	if obj is None:
		print("ERROR")
		print("end")
		return
	for attr in dir(obj):
		if attr[0] != '_':
			value = getattr(obj, attr)
			print("{}: {}".format(attr, value))
	print("end")
if __name__ == "__main__":
	obj = what_are_the_vars(7)
	doom_printer(obj)
	obj = what_are_the_vars("ft_lol", "Hi")
	doom_printer(obj)
	obj = what_are_the_vars()
	doom_printer(obj)
	obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
	doom_printer(obj)
	obj = what_are_the_vars(42, a=10, var_0="world")
	doom_printer(obj)
