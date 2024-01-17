#listas

my_list = ['Python',53,False,'hello world'] #cualquier tipo se puede poner
print(type(my_list)) #que tipo es, o sea, lista
print(my_list)
print(my_list[1]) #En programación se cuenta desde 0
print(my_list[0]) 
print(my_list[-1]) #cuenta al revez
print(my_list[-4])

my_list.append('5') #agregar cosas a la lista
print(my_list) #actualizada

my_list.insert(3, 'jaja') #poner en posición especifica pero quita el otro de esta posicion
print(my_list)

my_list.remove('hello world') #quitar un valor de la lista
print(my_list)

my_list.pop(2) #quitar dato de la posición indicada
print(my_list)

print(my_list.pop(2)) #quitar y decir que se ha removido
print(my_list)

print(my_list.count(2)) #contar cuantas veces se ha repetido un dato
#dice 0 pq no hay un 2

print(my_list.count(53))
print(my_list)

my_list.reverse #decir la lista al revez
print(my_list)

my_list.clear() #borrar los datos
print(my_list)

#fin
