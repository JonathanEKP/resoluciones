def calcularNumeroPrimo(numero):
    if numero>1:
        for n in range(2, num):
            if num % n == 0:
                print("No es primo", n, "es divisor")
                return False
        print("Es primo")
        return True
    else:
        print("El numero ingresado no es entero")


num = int(input("Escriba un numero para saber si es primo:"))
calcularNumeroPrimo(num)