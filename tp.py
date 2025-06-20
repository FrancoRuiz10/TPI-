from abc import ABC, abstractmethod

class Evaluar(ABC):
    @abstractmethod
    def nota(self):
        pass


class Persona:
    def __init__(self, nombre):
        self._nombre = nombre  

    
    def get_nombre(self):
        return self._nombre


class Estudiante(Persona, Evaluar):
    def __init__(self, nombre, nota_1=None, nota_2=None):  
        super().__init__(nombre)
        self._nota_1=nota_1
        self._nota_2=nota_2

    
    def resultado(self):
        self._nota_1=float(input(f"¿Cuál es la primera nota de {self._nombre}? "))
        self._nota_2=float(input(f"¿Cuál es la segunda nota de {self._nombre}? "))
        self._nota_final = (self._nota_1+self._nota_2)/2

   
    def decorar(func):
        def retornar(self, *args, **kwargs):
            print("*" * 50)
            print("ANALIZANDO NOTA...")
            print("*" * 50)
            return func(self, *args, **kwargs)
        return retornar

    @decorar
    def nota(self):
        if self._nota_1 == 0 or self._nota_2 == 0:
            return f"El alumno {self._nombre} debe recursar la materia por quedar libre"

        if self._nota_final >= 7:
            return f"El alumno {self._nombre} Promociona ya que su nota es {self._nota_final}"
        elif self._nota_final >= 4:
            return f"El alumno {self._nombre} Aprueba ya que su nota es {self._nota_final} debe rendir un examen final"
        else:
            return f"El alumno {self._nombre} Recursa ya que su nota es {self._nota_final} debe recursar la materia"
        



nombre1 = input("Ingrese el nombre del primer estudiante: ")
nombre2 = input("Ingrese el nombre del segundo estudiante: ")
nombre3 = input("Ingrese el nombre del tercer estudiante: ")

estudiante1 = Estudiante(nombre1)
estudiante2 = Estudiante(nombre2)
estudiante3 = Estudiante(nombre3)


estudiante1.resultado()
estudiante2.resultado()
estudiante3.resultado()


print(estudiante1.nota())
print(estudiante2.nota())
print(estudiante3.nota())
