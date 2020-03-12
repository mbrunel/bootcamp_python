# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    csvreader.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbrunel <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/12 07:16:15 by mbrunel           #+#    #+#              #
#    Updated: 2020/03/12 08:54:26 by mbrunel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class CsvReader():
	def __init__(self, name, sep=',', header=False, skip_top=0, skip_bottom=0):
		self.sep = sep
		self.header = header
		self.skip_top = skip_top
		self.skip_bottom = skip_bottom
		self.f = open(name)

	def __enter__(self):
		return self

	def __exit__(self, type, value, traceback):
		self.f.close()

	def getdata(self):
		return [e.split(',') for e in self.f.read().split('\n')[self.header + self.skip_top:-1-self.skip_bottom]]

	def getheader(self):
		if self.header:
			self.f.seek(0)
			return self.f.readline()

if __name__ == "__main__":
	with CsvReader('resources/good.csv', header=1, skip_top=2, skip_bottom=2) as file:
		print(file.getdata())
		print(file.getheader())
