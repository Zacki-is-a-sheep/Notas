#condiciones

if 4 < 6: #obligatorio los :    es como en un enunciado
        print('4 es menor que 6') #como si es verdadero el que 4 es menor que 6, lo imprime

if 4 > 6:
        print('4 es mayor que 6') #como no es verdad, no lo imprime
        
#a no ser que se agregue otra variable que haga que se imprima

numero = 7
if 4 > 6 or numero == 7:  #en resumen dice, si 4 es mayor que 6 o la variable numero es 7, entonces se debe imprimir
        print('4 es menor que 6, o numero = 7') #esto
        
Albion = 'Albion online es un mmorpg no lineal en el que escribes tu propia historia sin limitarte a seguir una historia lineal' #XD
if len(Albion) > 100: #si los caracteres (letras, espacios y números) que tiene la variable Albion son mayores a 100
        print('mucho texto bro') #en caso de que no sea mayor, no se imprimiria la variante
        
#si fuera if len(albion) < 100   o sea, imprimir la variante albion si los caracteres son menores a 100
#       print('mucho texto bro')     no se daria debido a que los caracteres de la variante albion son más de 100

if 4 > 6:
        print('cuatro es mayor que seis')
else: 
        print('no seas pendejo, como cuatro será mayor que seis')
#en resumidas cuentas lo que se hizo fue, si 4 es mayor que seis se debe de imprimir lo que dice el primer print
#pero si no es asi, entonces se debe de imprimir lo otro

#ahora viene el elif

if 24 > 42:
        print('24 es mayor que 42') #se pregunta si 24 es mayor a 42, y no es verdadero, entonces
elif numero == 7: #(revisa linea 11)    pregunta entonces si la variable numero es 7, como es verdadero imprime lo siguiente
        print('la variable numero es 7')
else:
        print('ninguna condición es correcta') #si lo anterior fuera incorrecto imprimiría esto
        
if 24 > 42:
        print('24 es mayor que 42') 
elif numero != 7: #en este caso anda preguntando si la variable numero es diferente a 7
        print('la variable numero es 7')
else:
        print('las anteriores condiciones eran erroneas') #como las dos anteriores eran falsas, ahora si pone esto
        
#if solo se puede uno (no en todo el codigo, se refiere que solo un if para cierta cosa, if e if no son en un mismo conjunto, como if elif else, if e if son completamente independientes)
#else puede haber uno o no
#elif son todos los que quieras, ya sea ninguno o un montón
