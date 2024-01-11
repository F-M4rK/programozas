mag=[]
f3=open("magasság.txt","r",encoding="utf-8")
for i in f3:
    kislista=i[:-1].split(",")
    mag.append(kislista)
f3.close()
print(mag)
