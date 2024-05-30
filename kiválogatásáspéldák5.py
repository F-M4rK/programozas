számok=[3,5,12,147,401,92,117,84,83,562]
#Írjuk ki az összes 200-nál nagyobb listaelemet
#1. megoldás:
print("1.megoldás: 200-nál nagyobb listaelemek:")
for i in range(0,len(számok)):
    if számok[i]>200:
        print(számok[i])
#2. megoldás:
print("2.megoldás: 200-nál nagyobb listaelemek:")
for szám in számok:
    if szám>200:
        print(szám)
