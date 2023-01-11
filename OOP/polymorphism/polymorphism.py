# polymorphism adalah method yang sama pada class yang berbeda

class Paus():
    def __init__(self,mangsa) -> None:
        self.mangsa = mangsa

    def makan(self):
        print(f"Paus makan {self.mangsa}")

class Harimau():
    def __init__(self,mangsa) -> None:
        self.mangsa = mangsa

    def makan(self):
        print(f"Harimau makan {self.mangsa}")
        


p = Paus("cumi")
p.makan()
h = Harimau("rusa")
h.makan()