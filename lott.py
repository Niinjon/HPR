import math
#szám nagyobb mint 5 listázzuk ki az összes olyan 5öst ami különbözik egymástól 

'''
szam = int(input("Adja meg a kezdő értéket"))
szam > 5

az=[1,2,3,4,5]  az[1]+=1 while az[1] == 90
'''

szam = int(input("Adj meg egy számot:"))
szamok = range(szam,91)

igen = []

for i in szamok:
    for j in szamok:
        if i == j:
            continue
        for k in szamok:
            if k in (i,j):
                continue
            for l in szamok:
                if l in (i,j,k):
                    continue
                for n in szamok:
                    if n in (i,j,k,l):
                        continue 
                    temp = {i,j,k,l,n}
                    if temp not in igen:
                        igen.append(temp)
                        
for x in igen:
    x = list(x)
    x.sort()
    print(x)

