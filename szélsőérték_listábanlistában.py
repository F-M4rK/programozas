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

#Adjuk meg, hogy melyik a névsorban utolsó város!
maxindex=0
for i in range(0,len(autózások)):
    if autózások[i][3]>autózások[maxindex][3]:
        maxindex=i
print("A névsorban utolsó városnév: ",autózások[maxindex][3])
