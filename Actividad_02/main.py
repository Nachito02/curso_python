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


calcularEdad()

