# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    matrix.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbrunel <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/12 01:29:34 by mbrunel           #+#    #+#              #
#    Updated: 2020/03/12 02:54:24 by mbrunel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Matrix:
	def __init__(self, data):
		if type(data) == tuple:
			self.shape = data
			self.data = [[0 for i in range(data[0])] for j in range(data[1])]
		elif type(data) == list:
			i = 1 
			self.data = [[]]
			try:
				elem = data[0]
			except:
				return
			while type(elem) == list:
				self.data.append(elem)
				try:
					elem = data[i]
				except:
					self.shape = (len(data), len(data[1]))
					del(self.data[0])
					return
				i += 1
			if elem == tuple:
				self.shape = elem

	def __str__(self):
		text = ''
		for l in self.data:
			text += str(l)
		return text

	def __add__(self, other):
		if type(self) == type(other) == Matrix:
			try:
				i = 0
				new = Matrix(self.shape)
				for i in range(self.shape[0]):
					for j in range(self.shape[1]):
						new.data[i][j] = self.data[i][j] + other.data[i][j]
				return new
			except:
				print("ERROR")

	def __radd(self, other):
		return self + other

	def __sub__(self, other):
		if type(self) == type(other) == Matrix:
			try:
				i = 0
				new = Matrix(self.shape)
				for i in range(self.shape[0]):
					for j in range(self.shape[1]):
						new.data[i][j] = self.data[i][j] - other.data[i][j]
				return new
			except:
				print("ERROR")
	def __rsub__(self, other):
		return self - other
