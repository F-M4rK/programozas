#A szavak lista tartalmazza, hogy az egyes oldalakon hány szó található
szavak=[750,610,1200,450,912]
#Adjuk meg, hogy összesen hány szó van az oldalakon: 1. megoldás
összeg=0
for i in range(0, len(szavak)):
    összeg=összeg+szavak[i]
print("1. megoldás: Összesen: "+str(összeg)+" szó található az összes oldalon.")

#Adjuk meg, hogy összesen hány szó van az oldalakon: 2. megoldás
összeg2=0
for szómennyiség in szavak:
    összeg2=összeg2+szómennyiség
print("2. megoldás: Összesen: "+str(összeg2)+" szó található az összes oldalon.")

#Adjuk meg, hogy összesen hány szó van az oldalakon: 3. megoldás

print("3. megoldás: Összesen: "+str(sum(szavak))+" szó található az összes oldalon.")


#------------------------
#Összegzés listában lista adatszerkezetben, amikor "oszlopban összegzünk":
magasságok=[["A1",180] , ["B18", 172] , ["C2", 168] , ["C3",164]]
# A magasságok lista elemeiben különböző kódjelzésű építőelemeinek
#magasságát tároljuk. Pl. az A'-es elem 180 cm magas.
#Ha egymás tetejére rakjuk ezeket mind, milyen magas lesz az építmény?
összmagasság=0
for i in range(0, len(magasságok)):
    összmagasság=összmagasság+magasságok[i][1]
print("A végső magasság: ", összmagasság, " cm lesz")

#ugyanez a legutóbbi másként megoldva:
hosszlista=[]
for i in range(0, len(magasságok)):
    hosszlista.append(magasságok[i][1])
print("A végső magasság a másik módszerrel: ", sum(hosszlista), " cm lesz")

