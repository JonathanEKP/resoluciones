import operaciones

a = int(input("Ingrese un numero:"))
b = int(input("Ingrese otro numero:"))
print()
print("La suma es:",operaciones.Calculadora.suma(a,b))
print("La resta es:",operaciones.Calculadora.resta(a,b))
print("La multiplicacion es:",operaciones.Calculadora.multiplicacion(a,b))
print("La division es:",operaciones.Calculadora.division(a,b))