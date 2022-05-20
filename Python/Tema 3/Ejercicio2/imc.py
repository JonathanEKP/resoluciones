peso = input("Cual es tu peso en kg?:")
altura = input("Cual es tu altura en metros?:")
indice = round(float(peso)/round(float(altura))**2,2)
print("Tu IMC es: "+str(indice))