folyók=["Duna","Tisza","Dráva","Szinva","Mura","Sió","Zala","Rábca"]
#Írjuk ki az összes olyan folyót, amelyiknek a neve tartalmaz "a" betűt
#1. megoldás:
print("1.megoldás:'a' karaktert tartalmazó folyók nevei:")
for i in range(0,len(folyók)):
    if folyók[i].find("a")>=0:
        print(folyók[i])
#2. megoldás:
print("2.megoldás:'a' karaktert tartalmazó folyók nevei:")
for folyó in folyók:
    if folyó.find("a")>=0:
        print(folyó)
