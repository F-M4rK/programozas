try:
    tev=[]
    f=open("evékenységek.txt.","r",encoding="utf-8")
    for sor in f:
            kislista=sor[:-1].split(";")
            tev.append(kislista)
except:
    print("Nem tudom beolvasni.")
