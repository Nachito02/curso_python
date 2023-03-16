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

def esPalindromo():
    string = input('Ingrese una palabra')
    if string == string[::-1]:
        return print('Es palindromo')
    else:
        return print('No es palindromo')


# esPalindromo()


#5. Diseñe e implemente una función en Python para la creación de direcciones de e-mail institucionales. 
# El usuario debe ingresar su nombre, apellido y el nombre de la empresa o institución a la que pertenece.
#  Las direcciones de e-mail institucionales constan de: la primera letra del nombre del usuario, 
# seguido de su apellido completo, seguido del @, seguido del nombre de la institución y por último un 
# .com. Toda la dirección de e-mail debe estar en minúscula.

def crearEmail():
    nombre = input('Ingresa tu nombre')
    apellido = input('Ingresa tu apellido')
    insitucion = input('Ingresa el nombre de la institucion')

    email = nombre[0] + apellido + "@" + insitucion +'.com'
    return print(email.lower())


# crearEmail()


# 6. Escriba un programa en Python para validar formatos de clave. 
# Para ello el programa debe permitir ingresar una clave y verifique que se cumplan los siguientes requisitos:
# Contener al menos una letra en mayúscula
# Contener al menos una letra en minúscula
# Contener al menos un número
# Contener al menos un caracter especial ( * / -  _ $ # %)



def validar_clave(clave):
    import re
    # Verifica que la clave cumpla con los requisitos
    if (len(clave) < 8):
        return False
    if not re.search("[a-z]", clave):
        return False
    if not re.search("[A-Z]", clave):
        return False
    if not re.search("[0-9]", clave):
        return False
    if not re.search("[* / - _ $ # %]", clave):
        return False
    return True



def encontrarSub():
    cadena = input("Ingrese una cadena de texto: ")
    subcadena = input("Ingrese una subcadena de texto a buscar: ")

    if subcadena in cadena:
        longitud = len(cadena)
        indice_subcadena = cadena.index(subcadena)

        if indice_subcadena < longitud/2:
            print(f"La subcadena '{subcadena}' se encuentra en la primera mitad de la cadena.")
        else:
            print(f"La subcadena '{subcadena}' se encuentra en la segunda mitad de la cadena.")
    else:
     print("La subcadena no se encuentra en la cadena.")




def sustituir():
    frase = "La división modular tiene sentido en problemas de cierta complejidad y tamaño. En problemas pequeños cuya solución se obtiene en forma casi inmediata o trivial no es necesario su planteo."
    print("Frase original: ", frase)

    # Reemplazar todas las ocurrencias de "problemas" por "situaciones"
    frase = frase.replace("problemas", "situaciones")

    print("Frase modificada: ", frase)



def precio(): 
    precio = float(input("Introduzca el precio del producto en pesos con dos decimales: "))

    # Obtener la parte entera y decimal del precio
    entero = int(precio)
    decimal = int((precio - entero) * 100)

    # Mostrar el resultado en pantalla
    print(f"{entero} pesos y {decimal} centavos")



def añoDeNacimiento():
    fecha_nacimiento = input("Ingrese su fecha de nacimiento en formato dd/mm/aaaa: ")

    # Separar la fecha en día, mes y año
    dia, mes, anio = fecha_nacimiento.split('/')

    # Mostrar el resultado en pantalla
    print(f"Día: {dia}")
    print(f"Mes: {mes}")
    print(f"Año: {anio}")