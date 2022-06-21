paises = input("Escriba los paises separados por coma: ")
lista = paises.split(',')
print(",".join(sorted(list(set(lista)))))