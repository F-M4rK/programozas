folyók=["Duna","Tisza","Dráva","Szinva","Mura","Sió","Zala","Rábca"]
#Írjuk ki az összes olyan folyót, amelyiknek a neve kevesebb mint 4 betűből áll
#1. megoldás:
print("1.megoldás: 5 karakterből álló folyók nevei:")
for i in range(0,len(folyók)):
    if len(folyók[i])<4:
        print(folyók[i])
#2. megoldás:
print("2.megoldás: 5 karakterből álló folyók nevei:")
for folyó in folyók:
    if len(folyó)<4:
        print(folyó)
