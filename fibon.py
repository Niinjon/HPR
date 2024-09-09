import math
import random

def fibon(n):
    return n if n<2 else fibon(n-2) + fibon(n-1)

a = int(input('Kezdoertek:'))#megadja melyik elemtől
b = int(input('Elem:'))#megadja hány elemet

az=[]
x=0
while True:
    temp=fibon(x)
    if temp>=a:
        az.append(temp)
    x+=1
    if x>b and len(az)==b:
        break
    
print(az)        
    
