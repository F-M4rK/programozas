#Megjegyzés: Mivel a méret megnevezése függ a térfogattól ,
#ezért nem szerencsés így megírni a konstriktort. Mert a mostani állapotában
#simán létre tudsz hozni olyan Sütemény példányt, amely pl. 300 köbcentiméteres
#de kicsi. Pedig ennek közepesnek kellene lennie a mi igényeink szerint.
#Próbáld meg átalakítani a konstruktort, hogy ne kérje be a méret paramétert,
#hanem  a térfogat segítségével határozd meg a levágás metódusban lévő kódhoz hasonlóan
#a méret nevű tulajdonságot.
class Sütemény:
    #Ez a Sütemény nevű objektumosztály
    def __init__(self,név,térfogat,méret,ízesítés,kinézet,recept_filenév):
        #ez a konstruktora (minden osztály konstruktorának __init__ a neve)
        self.név=név #a sütemény neve
        self.térfogat=térfogat #köbcentiméterben
        self.méret=méret #kicsi: térfogata 205 köbcentinél kisebb
        #205-1000 közötti: közepes,1000-nél nagyobb: nagy
        self.ízesítés=ízesítés #szöveges leírás a sütemény ízesítéséről
        self.kinézet=kinézet # szöveges leírás a sütemény kinézetéről
        self.recept_filenév=recept_filenév # a receptet tartalmazó fájl neve
        
    def levágás(self,mennyit):
        self.térfogat=self.térfogat-mennyit
        új_térfogat=self.térfogat
        if új_térfogat<205:
            self.méret="kicsi"
        elif új_térfogat<=1000:
            self.méret="közepes"
        else:
            self.méret="nagy"
    def get_ízesítés(self):
        return self.ízesítés


#Példánykészítés,  a konstruktor neve az osztály nevével fog megegyezni;
#a paraméterlistába itt már nem írjuk a self-et
s=Sütemény("csokis-marcipános",300,"közepes","csoki, marcipán","körcikk-hasáb", "csm.txt")

#Kiírom az ízesítését kétféleképpen:
print(s.ízesítés) #itt a tulajdonságot írom ki

print(s.get_ízesítés()) #itt meghívom a a get_ízesítés() metódust
#és az írja ki a tulajdonság értékét

#levágás előtt kiírjuk a térfogatot és méretet:
print("térfogat a vágás előtt:",s.térfogat)
print("méret a vágás előtt:",s.méret) 


#levágás: 60 köbcentit vágjunk le belőle
s.levágás(60)

#levágás után kiírjuk a térfogatot és méretet:
print("térfogat a vágás után:",s.térfogat)
print("méret a vágás után:",s.méret)

#Házi gyakorló feladatok:

#Készíts egy másik süteménytpéldányt!

#Vágj le belőle 100 köbcentimétert!

#Írd ki a receptet tartalmazó fájl nevét!
