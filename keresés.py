import math
#Keressük meg az első négyzetszámot
x=[6,2,44,3,8]
i=0
while i<=len(x)-1 and not round(math.sqrt(x[i]))==math.sqrt(x[i]) :
#A not szócska után a keresett tulajdonság fennállását kell megfogalmazni
#pl. ha az első 20-nál nagyobbat keresnnk, akkor ...and not x[i]>20: lenne
    i=i+1
if i<=len(x)-1:
    print("A keresett elem indexe: ",i)
    print("Az elsőnek megtalált keresett eleme: ",x[i])
else:
    print("nincs a keresett tulajdonságú elem a listában")
