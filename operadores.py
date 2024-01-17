#Operadores arimeticos

print(6 + 3)
print(6 - 3)
print(6 * 3)
print(6 / 3)

#Todo bien hasta acá pero agarra complejidad en

print(7 % 3) #Se le llama resto, 3 + 3 = 6 pero le falta 1 para 7 entonces ese es el resultado
print(9 % 3) #Queda 0 pq no queda nada 9 / 3 = 0

print(4 ** 3) #Exponencial 3 veces 4, mira
print(4 * 4 * 4)

print(11 // 3) #División de flor quita decimales (NO APROXIMA)
print(11 / 3)

print('siok' + 'entiendo') #texto se suma asi lol
print('siok' , 'entiendo') # agregaría un espacio
#no se pueden multiplicar entre letras, no jodas, pero si multiplicar las veces de un texto
print('Run ' * 10)
# print('Run ' + 10) no da Run 10, pero si se hace lo sig
print('Run ' + str(10)) #Ahora si sale Run 10 pq lo toma como texto (str) no como número (int) Aunque
print('Run ' + '11')  #Funciona igual XD pero con variables si se debe usar str
a = 12
print('Run ' + str(a))
print('Run ' + 'a')  #Pq si no lo toma como texto, lit la letra a

#Operadores comparativos
#Booleano dice si algo es verdadero o falso teniendo en cuenta los datos, true o false
print(4 < 8)
print(4 > 8)
print(4 == 8) #No un = pq si no estariamos dando un valor, el == es preguntar si son iguales
print(4 <= 8) #Menor o igual
print(4 >= 8) #Mayor o igual
print(4 != 8) #DIferente o igual

print('Respecto letras')

print('hola' > 'mundo') #se ve raro, no es por tamaño de caracteres
print('hola'> 'bolas') #cuenta donde estan posicionadas las letras del abecedario
print(len('hola')> len('bolas')) #si quisieramos que nos cuente los caracteres
print('a'> 'd') # a no es mayor que d pq a es la primera (1) letra del abecedario,la d es la cuarta (4)

print('Ahora')

#Operadores lógicos
print(4 < 6 and 7 > 9) # and    print(true and false) pregunta si es true y true, + * + = +   + * - = -
print(4 < 6 or 7 > 9) # or    print(true and false) si hay un true es true, independiente del false
print(not(4 < 6)) # not     negar algo que es cierto o falso 

print((not(7 != 7) and 6 > 5) and ('rozar' < 'rotar' or not(3 == 5)))
print('explicación')
print(not 7!= 7) #sin not, sería false
print(not 7 != 7 and 6 > 5) #si es true, este conjunto es true

print('rozar' < 'rotar') #z por su posicion es mayor que t, asi que es falso
print(not 3 == 5) # 3 no es igual a 5 pero gracias a not, da respuesta a la inversa
# el or como si ve un true, es true entonces
print ('true' and 'true')
