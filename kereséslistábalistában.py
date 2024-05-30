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

#Adjuk meg, hogy az elsőnek megtalált "János" autójának mi a rendszáma:
i=0 #kezdőindex, mert a 0-s indexűvel kezdjük a vizsgálatot
#n: lista elemszáma, (n-1) lesz az utolsó index a listában
n=len(autózások)
# a név a 2-es indexű helyen van az autózások[i] listában minden i-re
while i<=n-1 and not autózások[i][2]=="János":
    i=i+1
if i<=n-1:
    #ekkor megtaláltuk és az első talált elem index:i
    print(autózások[i][1])#az 1-es indexű helyen van a rendszám
else:
    print("Nincs János")
    
