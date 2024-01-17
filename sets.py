#sets

my_set = {}
print(type(my_set)) #diccionario ._.xd pq está vacío, se deben poner variables para que entienda que es un set

my_set = {'Python', 'JavaScript', 'C++'}
print(type(my_set)) #ahora si lo define como set

print(my_set) #no hay orden, repite varias veces y veras que da de formas diferentes en la consola, no importa el orden aqui
#si pides imprimir el 0 (el primer dato) no hay sentido pq ninguno es el primero ni el ultimo

my_set.add('C++')
print(my_set) #no acepta repetidos, no va a aparecer 2 veces o más

my_set.add('C#')
print(my_set)

my_set_0 = {'Python', 'JavaScript', 'C++'}
my_set.difference_update(my_set_0)
print(my_set) #da la diferencia de esos dos (my_set - my_set_0) , cual es el dato diferente

#fin
