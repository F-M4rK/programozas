#microbittel fényszinteket mértünk
fényszintek=[120,22,48,250,0,220]
#Írjuk ki a 150-es fényerősségnél fényesebb mérési eredményeket

for i in range(0,len(fényszintek)):
    if fényszintek[i]>150:
        print(fényszintek[i])
        
#Írjuk ki a képernyőre az összes fényszint számjegyeinek számát
def szj(szam):
    n=1
    while szam>=10**n:
        n=n+1
    return n





for elem in fényszintek:
    print(szj(elem))


színek=["piros","kék", "fehér","zöld","narancssárga"]
#Írjuk ki a képernyőre az összes színt és mellé, hogy nány karakterből áll a neve!
