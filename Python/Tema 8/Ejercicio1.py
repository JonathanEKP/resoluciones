file = open('archivo-ejercicio.txt', 'w')
file.write('Este es el archivo del ejercicio 1.\n')
file.close

file = open('archivo-ejercicio.txt', 'r+')
file.readline()
file.write('Escribiendo nuevamente.\n')

file.seek(0)
print(file.read())
file.close()