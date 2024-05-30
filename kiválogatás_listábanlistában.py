autózások=[] #ebbe a listába tesszük bele a fájl soraiból készült listácskákat
f=open("autóval.txt","r",encoding="utf-8")
#innentől kezdve f néven hivatkozunk a focieredmenyek.txtz fájlra
for sor in f:
    kislista=sor[:-1].split("|") # a fájl sorából készült lista
    #A fájl egy sorában az egyes adatok ;-vel vannak elválasztva
    autózások.append(kislista) #ezt a listácskát beletesszük a meccsek listába
f.close() #bezárjuk a fájl
#A fájl egy minta sora: Honda|CIV-123|János|Budapest
#Először az autó típusa, maj a rendszáma, a tulajdonos neve,
#a tuljadonos lakhelyének városa ilyen sorrendben | jellel (altgr-w) elválasztva

#Válogassuk ki az olyan autózásokat, ahol az autótípus neve
#tartalmaz "o" karaktert! Írjuk ki az autóneveket az ilyen esetekben!

for i in range(0,len(autózások)):
    if autózások[i][0].find("o")>-1:
        print(autózások[i][0])

print("-----------------")
#Válogassuk ki az olyan autózásokat, ahol az autótípus neve
#tartalmaz "o" karaktert! Írjuk ki az autótulajdonos nevét
#és az autó rendszámát vessző és szóközzel elválasztva!
for k in range(0,len(autózások)):
    if autózások[k][0].find("o")>-1:
        print(autózások[k][2]+", "+autózások[k][1])
