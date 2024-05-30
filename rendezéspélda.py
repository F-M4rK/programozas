x=[2,4,1,7,8,3,4,2,5]
for i in range(0, len(x)-1):
    for j in range(i+1, len(x)):
        if x[i]>x[j]:
            #csere
            seged=x[i]
            x[i]=x[j]
            x[j]=seged
        print(x)#ezt csak az ellenőrzéshez nézzük, hogy lássuk, milyen lépéseken keresztül megy a folyamat; ez nem kell
