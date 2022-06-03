import time

hora = time.strftime('%H')
minutos = time.strftime('%M')

if int(hora)>=19:
    print("Es hora de salir")
else:
    print("Aun no es tiempo de salir")