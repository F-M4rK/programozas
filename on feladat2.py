import math
try:
    x=float(input("Adj meg egy valós számot:"))
    y=math.sqrt(x)
    print(y)

except ValueError:
    print("annak nem lehet gyökét számolni a valós számok halmazában")
    

