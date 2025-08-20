#clase 6 e agosto del 2025
class clase:
    def __init__(self,atributo):
        #init va con dos guiones bajos al inicio y al final
        self.atributo = atributo

    def metodo(self):
        return f"El atributo es: " + self.atributo

    def imprimir(self):
        print("imprimiendo:" + self.atributo)
    
instancia = clase("valor") 
print(instancia.metodo() )  
instancia.imprimir() 
#crear una clase que sume dos numeros y los muestre por pantalla

class SumaNumeros:
    def __init__(self):
        self.numero1 = float(input("Por favor, ingrese el primer número: "))
        self.numero2 = float(input("Ahora ingrese el segundo número: "))

    def sumar(self):
        return self.numero1 + self.numero2

    def mostrar_suma(self):
        print ("La suma de ambos números da:", self.sumar())

instancia_suma = SumaNumeros()
instancia_suma.mostrar_suma()