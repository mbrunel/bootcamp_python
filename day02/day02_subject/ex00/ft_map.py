# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_map.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbrunel <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/12 04:11:06 by mbrunel           #+#    #+#              #
#    Updated: 2020/03/12 04:18:50 by mbrunel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_map(function_to_apply, list_of_inputs):
	"""copy of map function"""
	for i in range(len(list_of_inputs)):
		list_of_inputs[i] = function_to_apply(list_of_inputs[i])
	return list_of_inputs

