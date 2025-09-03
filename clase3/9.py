#clase 3/9
import csv
import json
class Persona:
    def__init__(self,name,ege,isStudent):
     self.name=Name
     self.age=age
     self.isStudent=isStudent
    def__srt__(self):
        return self.name + " " + self.isStudent

personas = []
with open ('data.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        persona = Persona(row[0],row[1],row[2])
        persona.appened(persona)
persona.pop(0)
for persona in personas:
   print(persona.__str__())
'''

{
    "name": "Jon Doe",
    "age":30
    "isStudent": false
}
'''
neme,age.isStudent
John Doe,30,false
'''