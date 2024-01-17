#diccionarios

my_dict = {'a', 'b'}
print(type(my_dict)) #dice que el tipo es set pq asi no son los dict en forma estructural

my_dict = {'Nombre':'Cristobal',
           'Apellido':'Colón',
           'Apodo':'tu mamá'} 

print(type(my_dict)) #ahora si dice que es dict
print(my_dict['Nombre']) #o sea, que busque en my_dict que nombre a que es igual

print(my_dict.keys()) #dice que palabras clave hay
print(my_dict.values()) #decir los datos
#se puede pasar a listas, tuplas o sets pero solo muestran las palabras clave
