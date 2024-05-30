számok=[3,5,12,147,401,92,117,84,83,562]
#Írjuk ki az összes 7-tel oszthatót a lista elemei közül
#1. megoldás:
print("1.megoldás: 7-tel osztható listaelemek:")
for i in range(0,len(számok)):
    if számok[i]%7==0:
        print(számok[i])
#2. megoldás:
print("2.megoldás: 7-tel osztható listaelemek:")
for szám in számok:
    if szám%7==0:
        print(szám)
