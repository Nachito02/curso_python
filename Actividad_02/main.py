# 1. Diseñe e implemente un programa en Python en donde se ingrese un número e informe:
# si es par o impar.
# si es múltiplo de 5.
# si es múltiplo de 3.
# si es múltiplo de 5 y 3 a la vez.

def esPar():

    numero = int(input('Introduce un numero'))
    if numero % 2 == 0:
     return 'Es Par'

    elif numero % 5 == 0 and numero % 3 == 0:
        return 'Es multiplo de 3 y de 5'

    elif numero % 5 == 0:
        return 'Es multiplo de 5'
    elif numero % 3 == 0:
        return 'Es multiplo de 3'


#print(esPar())


def precioPorEdad():
    numero = int(input('Ingrese su edad'))
    if numero >= 18:
        return 'Debes pagar $250'
    elif numero >= 4 and numero < 18:
        return 'Debes pagar $150'
    else:
        return 'Puedes pasar gratis'


#print(precioPorEdad())


def calcularMasaCorporal():
    peso = input('introduce tu peso en kg')
    estatura = input('introduce tu estatura')
    imc = int(peso) / float(estatura) ** 2

    if imc <= 18.5:
        return 'Bajo peso'
    elif imc >= 18.5 and imc <= 24.9:
        return 'Peso normal'

    elif imc >= 25 and imc <= 29.9:
        return 'Sobre peso'

    elif imc >= 30 and imc <= 34.9:
        return 'Obesidad tipo 1'

    elif imc >= 35 and imc <= 39.9:
        return 'Obesidad tipo 2'
    elif imc>=40:
        return 'Obesidad tipo 3'
    else :
        return 'Numero ingresado no valido'

    
#print(calcularMasaCorporal())


from datetime import datetime

def calcularEdad():
    fecha = input('Introduce tu fecha de nacimiento')

    fecha = datetime.strptime(fecha, '%d/%m/%Y')

    hoy = datetime.today()

    edad = hoy.year - fecha.year - 1

    print(edad)


#calcularEdad()

def cualesMayor():
    numero1 = int(input('Ingrese el primer numero'))
    numero2 = int(input('Ingrese el segundo numero'))
    numero3 = int(input('Ingrese el tercer numero'))

    if numero1 > numero2 and numero1 > numero3:
        return 'El numero mas grande es ',str(numero1)

    elif numero2 > numero1 and numero2 > numero3:
        return 'El numero mas grande es ', str(numero2)

    elif numero3 > numero2 and numero3 > numero1:
            return 'El numero mas grande es '+ str(numero3)




#print(cualesMayor())

def calculadora():
    numero1 = int(input('Ingrese el primer numero'))
    numero2 =   int(input('Ingrese el segundo numero'))

    operador = input("Ingrese + para sumar los números \n Ingrese  - para restar los números \n Ingrese * para multiplicar los números \n Ingrese / para calcular la división del primero con el segundo número \n Ingrese  P para calcular la potencia del primero elevado al segundo número "
)

    if operador == "+":
        return numero1 + numero2
    elif operador == "-":
        return numero1 - numero2

    elif operador == "*":
        return numero1 * numero2


    elif operador == "P":
        return numero1 ** numero2

        
    elif operador == "/":
        if numero2 == 0 or numero1 == 0:
            return 'no se puede divir por zero'
        else :
            return numero1 / numero2
   

 #print(calculadora())
import math

def calcRadio():


# Pedir al usuario los datos de la circunferencia y el punto
    radio = float(input("Ingrese el radio de la circunferencia: "))
    x_centro = float(input("Ingrese la coordenada x del centro de la circunferencia: "))
    y_centro = float(input("Ingrese la coordenada y del centro de la circunferencia: "))
    x_punto = float(input("Ingrese la coordenada x del punto: "))
    y_punto = float(input("Ingrese la coordenada y del punto: "))

    # Calcular la distancia entre el punto y el centro de la circunferencia
    distancia = math.sqrt((x_punto - x_centro)**2 + (y_punto - y_centro)**2)

    # Comparar la distancia con el radio de la circunferencia
    if distancia == radio:
        print("El punto está sobre la circunferencia")
    elif distancia < radio:
        print("El punto está dentro de la circunferencia")
    else:
        print("El punto está fuera de la circunferencia")

    
