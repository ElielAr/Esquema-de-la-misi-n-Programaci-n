# Impresión en pantalla print('Hola desde la consola')
from itertools import product


print('Hola desde la consola')

#Variables
sum = 1 +2
product = sum *2
print(product)

#Tipos de datos
#declaramos la variable
distancia_a_alfa_centauri = 4.367

# Descubrimos su tipo de dato
type(distancia_a_alfa_centauri)

# Importamos la biblioteca 
from datetime import date

# Obtenemos la fecha de hoy
date.today()

# Mostramos la fecha en la consola
print(date.today())

#Conversion tipo de datos
print ("Hoy es la fecha:" + str(date.today()))

#Recopilando informacion

print ("Bienvenido al programa de bienvenida")
name = input ("Introduce tu nombre")
print ("saludos:" + name)

#Trabajando con numeros
print("Calculadora")
num1 = input("Primer numero: ")
num2 = input("Segundo Numero: ")

print(int(num1)+int(num2))
