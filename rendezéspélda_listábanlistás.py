#Írjuk életkorok szerint rendezve a személyek nevét és életkorát!
életkorok=[ ["Gábor",17] ,["Emese",8] ,["Viktor",55], ["Tamás",89] ]
for i in range(0, len(életkorok)-1):
    for j in range(i+1, len(életkorok)):
        if életkorok[i][1]>életkorok[j][1]:
            #csere
            seged=életkorok[i]
            életkorok[i]=életkorok[j]
            életkorok[j]=seged

print("életkor szerint növekvően rendezve: ")
print(életkorok)
#Írjuk abc szerint rendezve a személyek nevét és életkorát!
életkorok=[ ["Gábor",17] ,["Emese",8] ,["Viktor",55], ["Tamás",89] ]
for i in range(0, len(életkorok)-1):
    for j in range(i+1, len(életkorok)):
        if életkorok[i][0]>életkorok[j][0]:
            #csere
            seged=életkorok[i]
            életkorok[i]=életkorok[j]
            életkorok[j]=seged
print("abc szerint rendezve: ")
print(életkorok)
