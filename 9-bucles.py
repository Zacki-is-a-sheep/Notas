#Bucles
# While es como un if pero que dice "esto se repetirá hasta que no se cumpla la condición"

#numero = 0
#while numero < 10:
#    print(numero)  se ejecuta infinitamente JLKSDJF

numero = 0
while numero < 10:
    numero += 1
    print(numero)
#lo que pasó fue que 0 al ser menor que 10 se imprimia, pero gracias a la sig linea se sumaba 1 cada vez que
#hasta que no se cumpla la condición, entonces, lit se puso a contar de 0 hasta el 10, porque 10 == 10, no 10 < 10

print('ahora a complicarse')

numero = 0
while numero < 10:
    numero += 1
    print(numero)
    if numero < 5:
        print('menor que 5')
print('ya se terminé de contar')

#lo que pasó fue, primero lo que hicimos al principio, pero como algunos numero eran menores a 5, cumpliendo
#la condicion de if, entonces tambien se colocaba el menor que 5
#al terminar la secuencia colocó el ultimo print

numero = 0
while numero < 10:
    numero += 1
    print(numero)
    if numero < 5:
        print('menor que 5')
        break #deja de contar, rompiendo el bucle

print('ya se encontró el 5')

lista = [2,3,5,7,11,13]
for number in lista:
    print(number)
print('respecto a la lista')

for number in range(11):
    print(number)
print('respecto a range')    

#vuelve a contar dentro de un rango, desde cero hasta el numero que indicamos (-1)
#o sea, le dijimos 11 pero cuenta hasta 10, pq lo toma como 11 caracteres y como cuenta desde 0
#es mejor que while numero < x numero y despues numero += 1
#siendo mas creativos

lista = [2,3,5,7,11,13]
for number in lista:
    print(number)
    
for number in range(11):
    print(number)
    if number == 9:
        print('aqui está el 9')
        break
print('ya es todo')
