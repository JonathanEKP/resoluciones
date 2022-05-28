
class Alumno():
    nota = None
    nombre = ""
    def __init__(self, nota: float, nombre:str):
        self.nombre = nombre
        self.nota = nota
        print()
        if self.nota >= 7:
            print("El nombre del alumno es:",self.nombre)
            print("La nota del alumno es:",self.nota)
            print("El alumno aprobo")
        elif self.nota >=0 or self.nota<7:
            print("El nombre del alumno es:",self.nombre)
            print("La nota del alumno es:",self.nota)
            print("El alumno Reprobo")
        else:
            print("La nota ingresada no es valida")




nota = float(input("Ingrese la nota:"))
nombre = input("Ingrese el nombre:")
a = Alumno(nota,nombre)
