# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata04.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbrunel <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/10 02:15:39 by mbrunel           #+#    #+#              #
#    Updated: 2020/03/10 02:27:19 by mbrunel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

phrase = "The right format"
print("{0}{1}".format("-" * (42 - len(phrase)), phrase))