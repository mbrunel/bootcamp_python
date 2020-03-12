# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    reduce.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbrunel <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/12 04:51:16 by mbrunel           #+#    #+#              #
#    Updated: 2020/03/12 05:08:54 by mbrunel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_reduce(function_to_apply, list_of_inputs):
	crook = function_to_apply(list_of_inputs[0], list_of_inputs[1])
	for e in list_of_inputs[2:]:
		crook = function_to_apply(crook, e)
	return crook
