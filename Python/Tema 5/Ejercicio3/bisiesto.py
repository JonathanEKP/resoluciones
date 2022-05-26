def bisiesto(year):
    if year % 4 != 0:
        print("No es bisiesto")
    elif year % 4 == 0 and year % 100 != 0:
        print("Es bisiesto")
    elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
        print("No es bisiesto")
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        print("Es bisiesto")



print()
y = int(input("Digite el año para comprobar si es bisiesto:"))
bisiesto(y)