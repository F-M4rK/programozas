#munkavégzéseket Joule-ban tartalmazza a munkák lista
munkák=[240,5, 500,300,5,120,12,40,800,5,34]
#Adjuk meg az első legkisebb munkamennyiséget!
minindex1=0
for i in range(1, len(munkák)):
    if munkák[i]<munkák[minindex1]:
        minindex1=i
print("Az első minimális elem indexe: ", minindex1)
print("Az első minimális elem értéke: ", munkák[minindex1])

#Adjuk meg az utolsó legkisebb munkamennyiséget!
minindex2=0
for i in range(1, len(munkák)):
    if munkák[i]<=munkák[minindex2]:
        minindex2=i
print("Az utolsó minimális elem indexe: ", minindex2)
print("Az utolsó minimális elem értéke: ", munkák[minindex2])

#Adjuk meg az első legnagyobb munkamennyiséget!
maxindex1=0
for i in range(1, len(munkák)):
    if munkák[i]>munkák[maxindex1]:
        maxindex1=i
print("Az első maximális elem indexe: ", maxindex1)
print("Az első maximális elem értéke: ", munkák[maxindex1])

#Adjuk meg az utolsó legnagyobb munkamennyiséget!
maxindex2=0
for i in range(1, len(munkák)):
    if munkák[i]>=munkák[maxindex2]:
        maxindex2=i
print("Az utolsó maximális elem indexe: ", maxindex2)
print("Az utolsó maximális elem értéke: ", munkák[maxindex2])

#egyszerű szélsőérték meghatározások
print("Minimális érték: ",min(munkák))
print("Maximális érték: ",max(munkák))

    
