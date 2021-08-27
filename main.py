# Codificado por @SantiagoUsach 27/07/2021


#Member ID's:
#Ingresar 111 para API1
#Ingresar 222 para API2
#Ingresar 333 para API3

import requests 
import json

url = 'https://raw.githubusercontent.com/santiagousach/codea-it/master/api.json'

r = requests.get(url)

apis = r.json()

mId = input("Ingrese su numero de miembro")

def checkMemberId(x):
    if mId == '111':
        print("Tu deductible es: ", apis["API1"]["deductible"])
        print("Tu stop loss es: ", apis["API1"]["stop_loss"])
        print("Tu oop max es: ", apis["API1"]["oop_max"])
    elif mId == '222':
        print("Tu deductible es: ", apis["API2"]["deductible"])
        print("Tu stop loss es: ", apis["API2"]["stop_loss"])
        print("Tu oop max es: ", apis["API2"]["oop_max"]) 
    elif mId == '333':
        print("Tu deductible es: ", apis["API3"]["deductible"])
        print("Tu stop loss es: ", apis["API3"]["stop_loss"])
        print("Tu oop max es: ", apis["API3"]["oop_max"]) 
    else:
        print("El numero ingresado no es valido")


while mId == ('111') or ('222') or ('333'):
    checkMemberId(mId)
    mId = input("Ingrese su numero de miembro")
