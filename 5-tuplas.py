#tuplas
#muy similares a las listas

my_tupla = (41, 'perro', 7.4, True) #parentesis normal lol
print(type(my_tupla)) #dice que es una tupla

print(my_tupla[1])
print(my_tupla.count(41)) #contar las veces que está
print(my_tupla.index('perro')) #decir que posición está

#no se puede añadir mas cosas a no ser de que convertimos tupla a list

my_tupla = list(my_tupla)
print(type(my_tupla))

my_tupla.pop() #quita el ultimo
print(my_tupla)

my_tupla = tuple(my_tupla)
print(type(my_tupla))
print(my_tupla)

#ya
