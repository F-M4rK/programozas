def f1(x):
    import math
    return math.sqrt(5*x+2)


def e1():
    #bejérós ciklussal
    for i in madarak:
        if i[-2]=="g":
            print(i)

def e2():
    #számlálos ciklussal
    for y in range(0,len(madarak)):
        if madarak[y][-3]=="e":
            print(madarak[y])



#Főprogram
print("f1(41):",f1(41))
f14érték=f1(41)

madarak=["cinege","fecske","sirály","gólya","széncinege"]
e1()
e2()
