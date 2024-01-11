#válogassuk ki a 20 -és 30  (20 -és 30 nem) közötti értékeket és tegyük be egy új listába
w=[8,3,5,2,25,12,35,20, 12,30,27]
#másik lista p
p=[]
#p=p+[w[5]]
for i in range (0,len(w)):
    if w[i]>20 and w[i] <30:
        #print(w[i])
        p=p+[w[i]]
        print(p)
