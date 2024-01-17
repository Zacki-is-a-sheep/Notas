#un comentario que no afecta en nada al código

print('Hola Mundo') #pedirle a la consola que imprima lo que está en comillas

# Tipos de datos

print(type('inserte texto')) #str es palabras
print(type(9)) #int es números enteros 
print(type(4.5)) #float es números decimales
#en núm no hay que poner '' o si no lo marcará como str 

# Variables

a = 4 #Básicamente, ecuaciones, darle un valor a x dato
print(a)
print('a') #Con comillas pasa de ser variable a un texto
b = 6
c= a + b #Todo normal, sumar es sumar, ni modo que sea un dividir
print(c)

mi_texto = 'Texto random' #snake_case: forma de escribir en variables que espacio se reemplaza con _
print(type (mi_texto))
mi_número = 9 #Es un número, no un texto asi que NO ''

print(mi_texto, mi_número) #Texto random 9
# print(mi_texto + mi_número) variables no se suman así, daría can only concatenate str (not "int") to str
print('Mi número favorito es:', mi_número)
