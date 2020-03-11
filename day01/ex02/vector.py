# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    vector.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbrunel <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/11 08:12:10 by mbrunel           #+#    #+#              #
#    Updated: 2020/03/11 09:32:42 by mbrunel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class Vector:
	def __init__(self, data):
		self.size = -1 
		self.values = [0]
		try:
			if type(data) == list:
				self.values = [float(i) for i in data]
				self.size = len(data)
			elif type(data) == tuple and data[0] > 0 and data[1] > data[0]:
				self.values = [float(i) for i in range(data[0], data[1] - 1)]
				self.size = data[1] - data[0]
			elif type(data) == int and data > 0:
				self.values = [float(i) for i in range(data - 1)]
				self.size = data
		except:
			pass

	def __str__(self):
		if self.size == -1:
			return "ERROR"
		return (str(self.values))

	def __add__(self, other):
		if self.size == -1:
			return Vector(-1) 
		if type(other) == int:
			return Vector([i + other for i in self.values])
		else:
			try:
				if (other.size == self.size):
					return Vector([self.values[i] + other.values[i] for i in range(other.size - 1)])
				else:
					return Vector(-1)
			except:
				return Vector(-1)

	def __radd__(self, other):
		return self + other

	def __sub__(self, other):
		if self.size == -1:
			return Vector(-1) 
		if type(other) == int:
			return Vector([i - other for i in self.values])
		else:
			try:
				if (other.size == self.size):
					return Vector([self.values[i] - other.values[i] for i in range(other.size - 1)])
				else:
					return Vector(-1)
			except:
				return Vector(-1)

	def __rsub__(self, other):
		return self - other

	def __truediv__(self, other):
		if self.size == -1:
			return Vector(-1) 
		if type(other) == int and other != 0:
			return Vector([i / other for i in self.values])
		else:
			return Vector(-1)

	def __rtruediv__(self, other):
		return self / other

	def __mul__(self, other):
		if self.size == -1:
			return Vector(-1) 
		if type(other) == int:
			return Vector([i * other for i in self.values])
		else:
			try:
				if (other.size == self.size):
					return sum([self.values[i] * other.values[i] for i in range(other.size - 1)])
				else:
					return Vector(-1)
			except:
				return Vector(-1)

	def __rmul__(self, other):
		return self * other
