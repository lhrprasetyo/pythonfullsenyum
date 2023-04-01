# polymorphism adalah method yang sama pada class yang berbeda

class Paus():
    def __init__(self,mangsa) -> None:
        self.mangsa = mangsa

    def makan(self):
        return (f"Paus makan {self.mangsa}")

class Harimau():
    def __init__(self,mangsa) -> None:
        self.mangsa = mangsa

    def makan(self):
        return (f"Harimau makan {self.mangsa}")

class Kambing():
    def __init__(self,mangsa) -> None:
        self.mangsa = mangsa

    def makan(self):
        return (f"Kambing makan {self.mangsa}")
        


p = Paus("cumi")
p.makan()
h = Harimau("rusa")
h.makan()
k = Kambing("daun")
k.makan()

for a in [p,h,k]:
    print(a.makan())