# Guía de Actividades No. 3 - Estructuras iterativas
# 1. Escriba un programa en Python donde el usuario ingrese un número natural positivo y muestre por consola todos los valores impares desde 1 hasta el número ingresado.



def numerosImpares():
   numero = int(input('Ingrese un numero natural positivo'))

   for i in range(1, numero+1):
            if i % 2 !=0:
             print(i)
        
# numerosImpares()

# 2. Escriba un programa en Python donde el usuario ingrese números naturales, se sumen y se muestre el resultado por pantalla. Para que el usuario deje de añadir números a la suma debe ingresar el valor -1

def sumarNumeros():
    suma = 0
    numero = 0

    while numero != -1:
        numero = int(input('ingrese los nuermos a sumar, para completar la suma -1'))
        if(numero != -1):        
            suma +=numero
            print('El resultado de la suma es ', suma)

        
# sumarNumeros()

# 3. Escriba un programa que pregunte cuántos números se van a introducir, pida esos números e informe el mayor, el menor y el promedio.

def MenorMayorPromedio():
    numero = int(input('Cuantos numeros decide introducir?'))
    lista= []
    for i in range(numero):
        apend = int(input('Igrese su numero: '))
        lista.append(apend)

    numero_maximo = max(lista)
    numero_minimo = min(lista)
    numero_promedio = int(sum(lista) / len(lista))
    print(f'el numero maximo es : {numero_maximo}')
    print(f'el numero minimo es : {numero_minimo}')
    print(f'el numero promedio es : {numero_promedio}')



# # MenorMayorPromedio()

# 4. Una Empresa paga a sus 100 operarios semanalmente de acuerdo con la cantidad de horas trabajadas, a razón de 300 pesos la hora hasta 40 hs. y un 50% más por todas las horas que pasan de 40. Se debe solicitar al usuario la cantidad de horas trabajadas por cada operario. Informar el salario de cada trabajador y el total del dinero que debe abonar la empresa.


# 5. Exhibir en pantalla 50 datos numéricos generados al azar entre 1 y 5000. Obtener como salida los siguientes parámetros estadísticos:

# a) el promedio
# b) los 2 mayores
# c) el menor de la lista.

import random 
import statistics
numeros = []
def cincuentaDatos():
    for i in range(50):    
        numeros.append(random.randint(1,5000))

    promedio = statistics.mean(numeros)
    mayores = sorted(numeros,reverse=True)[:2]
    menor = min(numeros)

    print(f"El numero promedio es {int(promedio)}")
    print(f"Los 2  numeros mayores son {mayores}")
    print(f"El numero menor es  {int(menor)}")


# cincuentaDatos()


# 6. Diseñe e implemente un programa en Python que lea un número entero e informe si es primo o no.

def esPrimo():
    numero = int(input('ingrese su numero'))
    if numero <= 1:
        return 'Su numero no es primo'
    for i in range(2, numero, 1):
        if(numero % i == 0):
            return 'Su numero no es primo'
        else :
            return 'Su numero es primo'


# print(esPrimo())