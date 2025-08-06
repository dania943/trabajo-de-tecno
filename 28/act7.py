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
