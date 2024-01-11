időj=[]
f1=open("időjárás.txt","r",encoding="utf-8")
for i in f1:
    kislista=i[:-1].split(";")
    időj.append(kislista)
f1.close()
print(időj)
