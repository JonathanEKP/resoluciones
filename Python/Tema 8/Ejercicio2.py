from pickle import *

class Vehiculo:

    def __init__(self, color):
        self.color = color
    
    def __str__(self):
        return self.color


coche = Vehiculo("Rojo")

file = open('VehiculoObj.txt', 'w+b')

dump(coche, file)
file.seek(0)

nuevo_coche = load(file)

print(nuevo_coche)
file.close()