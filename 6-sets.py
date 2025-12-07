# Sets, capítulo 1: Sin orden.
my_set = {} 
print(type(my_set)) # Diccionario ._.xd 
print()
# Esto se debe a que está vacío.
# Pues no hay elementos en el conjunto.

my_set = {'Python', 'JavaScript', 'C++'}
print(type(my_set)) # Ahora si lo define como set.
print()

# O también tenemos set(['Python', 'JavaScript', 'C++'])
# El orden no importa, pues se imprime de formas diferentes cada vez.
# Si intentas imprimir el primer elemento (el 0), no tiene sentido,
# ya que no hay un primer ni un último elemento en un conjunto.
print(my_set) 
print()


my_set.add('C#')
print(my_set) # El conjunto sigue siendo {'Python', 'JavaScript', 'C++'},
              # porque 'C++' ya estaba en el conjunto.
print()


# La función difference_update() actualiza el conjunto actual restándole otro conjunto.
# Esto significa que elimina del conjunto actual los elementos que también están en el otro conjunto.
my_set_0 = {'Python', 'JavaScript', 'C++'}
print(my_set.difference_update(my_set_0))
print()

print("Difference Update: Restar otro conjunto al conjunto actual")
print(my_set) # {'C#'} ya que 'Python', 'JavaScript' y 'C++' han sido eliminados
print()
