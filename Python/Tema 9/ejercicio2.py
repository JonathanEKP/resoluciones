from functools import reduce

numeros = [1, 3, 60, 26, 55, 100, 25, 12]

def numImpar(x):
    if x % 2 != 0:
        return True
    
    return False

def suma(a, b):
    return a+b


filtro = filter(numImpar, numeros)
respuesta = reduce(suma, filtro)
print("La suma de los numeros impares de la lista es:",respuesta)