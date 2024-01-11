kutyák=["Husky","bordercolli","Németjúhász","Chauchau"]
#1.Írjuk ki az összes kutyafajta nevét a képernyőre egymás alá!

#1.a számlálós ciklussal
for i in range(0,len(kutyák)):
    print(kutyák[i])

print("-----------------")

#1.b bejárós ciklussal
for elem in kutyák:
    print(elem)

print("-----------------")

#1.c feltételes ciklussal (elöltesztelős)
számláló=0
while számláló<=len(kutyák)-1:
    print(kutyák[számláló])
    számláló= számláló+1

print("-----------------")
print("1.feladat vége")
print("-----------------")

#2.Írjuk ki az összes kutyafajta nevének utolsó
#betűiből képzett szót a képernyőre

#2.a számlálós ciklussal
szó_a=""
for i in range(0,len(kutyák)):
    szó_a=szó_a+kutyák[i][-1]
print(szó_a)

print("-----------------")

#2.b bejárós ciklussal
szó_b=""
for elem in kutyák:
    szó_b=szó_b+elem[-1]
print(szó_b)

print("-----------------")

#2.c feltételes ciklussal (elöltesztelős)
számláló2=0
szó_c=""
while számláló2<=len(kutyák)-1:
    szó_c=szó_c+kutyák[számláló2][-1]
    számláló2= számláló2+1
print(szó_c)
print("-----------------")
print("2.feladat vége")
print("-----------------")
