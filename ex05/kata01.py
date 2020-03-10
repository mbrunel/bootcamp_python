# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    kata01.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mbrunel <marvin@42.fr>                     +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/10 01:43:53 by mbrunel           #+#    #+#              #
#    Updated: 2020/03/10 01:58:22 by mbrunel          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

languages = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

for e in languages:
	print(e, " was created by ", languages.get(e))
