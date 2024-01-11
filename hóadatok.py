hóadatok=[]
f=open("havak.txt","r",encoding="utf-8")
for sor in f:
    kislista=sor[:-1].split(";")
    hóadatok.append(kislista)
f.close()
