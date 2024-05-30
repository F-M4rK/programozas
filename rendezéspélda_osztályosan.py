class Adatsor:
    def __init__(self,név,életkor):
        self.név=név
        self.életkor=életkor

adatok=[] #ez lesz a listám az Adatsor példányaiból
adatsor1=Adatsor("Gábor",17)
adatsor2=Adatsor("Emese",8)
adatsor3=Adatsor("Viktor",55)
adatsor4=Adatsor("Tamás",89)
adatok.append(adatsor1)
adatok.append(adatsor2)
adatok.append(adatsor3)
adatok.append(adatsor4)
#Írjuk életkorok szerint rendezve a személyek nevét és életkorát!
for i in range(0, len(adatok)-1):
    for j in range(i+1, len(adatok)):
        if adatok[i].életkor>adatok[j].életkor:
            #csere
            seged=adatok[i]
            adatok[i]=adatok[j]
            adatok[j]=seged

for adat in adatok:
    print(adat.név, adat.életkor)
#Írjuk abc szerint név szerint rendezve a személyek nevét és életkorát!
for i in range(0, len(adatok)-1):
    for j in range(i+1, len(adatok)):
        if adatok[i].név>adatok[j].név:
            #csere
            seged=adatok[i]
            adatok[i]=adatok[j]
            adatok[j]=seged

for adat in adatok:
    print(adat.név, adat.életkor)
