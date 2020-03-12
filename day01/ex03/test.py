# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    test.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbrunel <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/12 01:28:36 by mbrunel           #+#    #+#              #
#    Updated: 2020/03/12 02:54:26 by mbrunel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from matrix import Matrix

matrix = Matrix([[1, 2, 3], [4, 5, 5], [6, 7, 6]])
print(matrix)
print(matrix.shape)
print(matrix + matrix)
print(matrix - matrix - matrix)
