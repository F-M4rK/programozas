vár=[]
f2=open("városok.txt","r",encoding="utf-8")
for i in f2:
    kislista=i[:-1].split(";")
    vár.append(kislista)
f2.close()
print(vár)
