#tantárgyak listát a tulajdonságok szótárat

with open('igen.txt','r',encoding="utf-8") as file:
    f=file.readlines()
    
asd = {}
sda = []
for line in f:
    s=line.split(',')
    sda.append(s)
    for x in sda:
       pass #print(x)
    #print("")
asd[sda[0][0]] = sda[1][0]

print(asd)

    
    
    
