import math

#megadott számtól nem nagyobb prímek 

#text=open("nem.txt","w")
szam = int(input("Adj meg egy számot:"))

def prim(szam):
    primsz=True
    for x in a:
        if szam%x == 0:
            primsz = False
    
    return primsz

a = [2,3,5,7,9]

for x in range(10,szam+1):
    if prim(x):
        a.append(x)

print(a)
'''
for x in range(2,szam + 1):
    if x%2 != 0 and x%3 != 0 and x%5 != 0 and x%7 != 0:
        a.append(x)    
'''

'''
text.write(str(a))


text.close()
'''