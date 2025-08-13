#clase 13 de agosto
class Padre:
    apellido=""
    def __init__(self,nombre):
        self.nombre=nombre

class Hijo(Padre):
    def __init__(self,nombre,apellido,lenguajeDeProgramacion):
        super().__init__(nombre,apellido)
        self.lenguajeDeProgramacion=lenguajeDeProgramacion

padre=Padre("nombre del padre")
Padre.apellido="apellido del padre"
hijo=Hijo("nombre del hijo","python")
print(hijo.nombre,hijo.apellido)