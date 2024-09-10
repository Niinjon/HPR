import math
#szám nagyobb mint 5 listázzuk ki az összes olyan 5öst ami különbözik egymástól 

'''
szam = int(input("Adja meg a kezdő értéket"))
szam > 5

az=[1,2,3,4,5]  az[1]+=1 while az[1] == 90
'''

szam = int(input("Kezdoertek ( >5 ):"))

ez=[]
az=[]

while ez[]:
    if szam > 5:
        for i in range(5):
            szam += 1
            az.insert(0,szam)
            if az[0] == 90:
                pass
    else:
        szam = int(input("Kezdoertek ( >5 ):"))

