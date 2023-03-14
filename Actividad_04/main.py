# 1. Diseñe e implemente un programa en Python que pida al usuario que ingrese su nombre. El programa debe saludar al usuario imprimiendo por pantalla el mensaje “Saludos <usuario>”, donde se debe reemplazar <usuario> por el nombre ingresado.


def saludarUser():
    nombre = input('Ingrese su nombre \n')

    print(f"Hola {nombre}")


# saludarUser()

# 2. Escribir un programa en Python en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

def cuantasLetras():
    frase = input('Ingrese una frase')
    letra = input('Ingrese una letra')

    contador = 0
    for i in frase:
        if i == letra:
            contador += 1
    return print(f'La letra {letra} aparece {contador} en la frase')


# cuantasLetras()

# 3. Escriba un programa que permita al usuario leer una cadena de caracteres y exhiba un menú con las opciones:
# Pasar a Mayúsculas
# Pasar a Minúsculas
# Solo la inicial con mayúsculas


def cadenaConvertida() : 

    cadena = input('Ingrese una cadena de texto')

    print("\nSelecciona una opción:")
    print("1. Pasar a Mayúsculas")
    print("2. Pasar a Minúsculas")
    print("3. Solo la inicial con mayúsculas")
    print("4. Salir")

    opcion = int(input('Ingrese el numero deseado'))

    if opcion == 1:
        return print(f'tu cadena quedo asi {cadena.upper()}')
    if opcion ==2:
        return print(f'tu cadena quedo asi {cadena.lower()}')
    
    if opcion ==3:
        return print(f'tu cadena quedo asi {cadena.capitalize()}')
    
    if opcion ==4:
        print('Saliendo del programa')
        return

# cadenaConvertida()

# 4. Escribir un programa en Python que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

