# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata04.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbrunel <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/10 02:27:37 by mbrunel           #+#    #+#              #
#    Updated: 2020/03/10 02:47:46 by mbrunel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

t = ( 0, 4, 132567.42222, 10000, 12345.67)
print("ex_04 : ", end = '')
for e in t:
	if e != t[0]:
		print(",", end = ' ')
	print(f"{e:3e}", end = '')
print('')
