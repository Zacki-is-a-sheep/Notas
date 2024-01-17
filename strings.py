#Strings

my_first_string = "mi string con comillas dobles"
my_second_string = 'mi string con comillas simples'

#print(my_first_string, my_second_string)
#print('esto es un texto ' + my_first_string + ' ' + my_second_string)
#queda muy pesado, entonces es mejor:
print(f'esto es un texto {my_first_string} y esto es la otra parte del texto')

other_string = 'hola'
a,b,c,d = other_string 

print(a)
print(b)
print(c)
print(d)
print(f'{a} {b} {c} {d}')

print(my_first_string.upper()) #Todo en mayus
print(my_first_string.capitalize()) #poner primera letra en mayus
print(my_first_string.lower()) #Todo en minus
print(len (my_first_string)) #cuantas letras tiene la variable
print(my_first_string.find('f')) #encontrar letras, no hay en este caso por eso el menos 1
print(my_first_string.find('r')) #en la posición 5 está la r
print(my_first_string.count('l')) #contar las veces que está la letra o número
print(my_first_string.upper().isupper) #pregunta si todo está en mayus, es true
print(my_first_string.lower().isupper) #falso, todo está en minus

#es todo
