print("ingrese un numero")
numero1=int(input())
#print("ingrese otro numero")
numero2=int(input("ingrese otro numero"))
suma=(numero1+numero2)
print("la suma de estos numeros da",suma)
menor= numero1 < numero2    
mayor= numero1 > numero2
igual= numero1 == numero2
#igual ==
#print("tal es mayor que tal",suma)
if mayor:
    print("numero1 es mayor que numero2")
if igual:
    print("numero1 es igual que numero2") 
if menor:    
    print("numero1 es menor que numero2")

lista = [0,1,2,3,4,5,6,7]
for elemento in lista[:]:
    lista [elemento]=elemento*2
    print(lista[elemento],end=",")
print("")

4
for x in range(1,7,2):
      print(lista[x])

