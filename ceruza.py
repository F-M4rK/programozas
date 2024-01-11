class Ceruza:

    def __inti__(self,szín,méret):
        self.szín=szín
        self.méret=méret #5cm rövid, 10cm közepes, 15cm+ hosszú

    def faragás(self,mennyit):
        self.méret=méret-mennyit
        új_méret=self.méret
        if új_méret <5:
            self.méret="rövid"
        elif új_méret <=10:
            self.méret="közepes"
        else:
            self.méret="hosszú"
    def get_szín(self):
        return self.szín

c=Ceruza("kék",10)

print(s.szín)

print(s.get_szín())

print("ceruza hossza faragás előtt:" s.méret)

s.faragás(2)

print("ceruza hossza faragás után:" s.méret)
