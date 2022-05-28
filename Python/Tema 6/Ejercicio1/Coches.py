from turtle import color


class Vehiculo():
    color="Rojo"
    ruedas = "Deportivas"
    puertas = 4



class Coche(Vehiculo):
    velocidad = "120Km/h"
    cilindrada = 4





c = Coche
print("El color del coche es:",c.color)
print("El tipo de ruedas del coche es:",c.ruedas)
print("Las puertas del coche son:",c.puertas)
print("La velocidad del coche es:", c.velocidad)
print("La cilindrada de un coche es:",c.cilindrada)