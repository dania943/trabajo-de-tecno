#clase 17 de septiembre
from enum import Enum, auto

class Baraja(Enum)
    pass
class Española(Baraja)
    ORO = auto()
    COPA = auto()
    ESPADA = auto()
    BASTO = auto()
class Francesa(Baraja):
    TREBOL = auto()
    DIAMANTE = auto()
    ESPADA = auto()
    CORAZONES = auto()
class Numero(Enum):
    DOS =2
    TRES =3
    CUATRO = 4
    CINCO =5
    SEIS = 6
    SIETE = 7
    OCHO = 8
    NUEVE =9
classNumeroEs(Numero):
    AS=1 
    SOTA=10 
    CABALLO=11 
    REY=12
class NumeroEs(Numero)
    A=1
    DIEZ =10
    J =11
    Q =12
    K =13
class Carta:
    def__init__(self,tipo,numero):
    self.tipo=tipo
    self.numero=numero
nueveDeEspada=Carta(española.ESPADA,9)
print(Española(1).name)