# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_filter.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbrunel <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/12 04:19:05 by mbrunel           #+#    #+#              #
#    Updated: 2020/03/12 04:50:34 by mbrunel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_filter(function_to_apply, list_of_inputs):
	return [e for e in list_of_inputs if function_to_apply(e)]
