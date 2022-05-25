
import math


def calcularAreaTriangulo(base, altura):
    resultado = (base*altura)/2
    print("El area del triangulo es:",resultado)
    


def calcularAreaCirculo(r):
     
    resultado = math.pi*(r**2)
    print("El area del circulo es:", resultado)




base = int(input("Ingrese la base del triangulo:"))
altura = int(input("Ingrese la altura del triangulo:"))
radio = int(input("Ingrese el radio del circulo:"))

print()
calcularAreaTriangulo(base, altura)
calcularAreaCirculo(radio)