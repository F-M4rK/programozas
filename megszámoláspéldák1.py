folyók=["Duna","Tisza","Dráva","Szinva","Mura","Sió","Zala","Rábca"]
#Hány olyan folyó van, amelyiknek a neve tartalmaz "a" betűt
#1. megoldás:
print("1.megoldás:'a' karaktert tartalmazó folyók darabszáma:")
db1=0
for i in range(0,len(folyók)):
    if folyók[i].find("a")>=0:
        db1=db1+1
print(db1)
#2. megoldás:
print("2.megoldás:'a' karaktert tartalmazó folyók darabszáma:")
db2=0
for folyó in folyók:
    if folyó.find("a")>=0:
        db2=db2+1
print(db2)
