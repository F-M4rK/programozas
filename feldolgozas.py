tev=[]
f=open("tevékenységek.txt.","r",encoding="utf-8")
for sor in f:
    kislista=sor[:-1].split(";")
    tev.append(kislista)
f.close()
#Írjuk egymés alá az összes tevékenység időtartamot
for i in range(0,len(tev)):
    print(tev[i][0])
