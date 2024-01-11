h=open("sz2.txt","w",encoding="utf-8")
for i in range(150,251,5):
    h.write(str(i))
    h.write("\n")
h.close()
