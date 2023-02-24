
# ejercicio 2
import math
entero = 10
flotante = 2.3
flotante_cientifica = 2e+2
string = 'hola'
bol = True

print(entero)
print(flotante)
print(flotante_cientifica)
print(string)
print(bol)

#  #ejercicio 3

# devolver valor numerico a pies
metro = input('ingrese un valor en metros')
metro = int(metro) * 0.3048
print("el valor en pies es: " + str(metro))

# Saludar usuario
nombreUsuario = input('Ingrese su nombre: ')
print('Hola! ' + nombreUsuario)

# ejercicio 3
radio = input('Introduce el perimetro')

# calcular area
area = 2 * math.pi
print('El area es ', area)

# calcular perimetro
perimetro = area * int(radio) ** 2
print('El perimetro es ', perimetro)

print('vamos a calcular tu masa corporal :)')

peso = input('introduce tu peso en kg')
estatura = input('introduce tu estatura')
imc = int(peso) / float(estatura) ** 2
print('tu masa corporal es ', imc)

# conocer cuanto le cuesta el combustible


odo_i = int(input('ingrese el valor inicial del odometro: '))
odo_f = int(input('ingrese el valor final del odometro: '))


consumo_prom = float(input('consumo promedio: (listros por cada km) '))


precio_combustible = float(input('precio del combustible'))

km_recorrido = odo_f - odo_i

litros_consumidos = km_recorrido * consumo_prom

precio_viaje = precio_combustible * litros_consumidos

print("El costo del viaje es :", precio_viaje)
