"""
Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом
 по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

*Пример:*

3 2 4 -> yes
3 2 1 -> no
"""

size_choko = [int(i) for i in input('Введите размер шоколадки n × m через пробел: ').split()]
size_split = int(input('Введите количество получаемых долек: '))
if ((size_split >= size_choko[0]) and (size_split % size_choko[0] == 0)) or ((size_split >= size_choko[1]) and
                                                                             (size_split % size_choko[1] == 0)):
	print('yes')
else:
	print('no')
