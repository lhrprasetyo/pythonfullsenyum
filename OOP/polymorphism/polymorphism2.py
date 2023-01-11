class Ayam():
    def __init__(self,alat) -> None:
        self.nafas = alat

    def bernafas(self):
        print(f"Ayam bernafas dengan {self.nafas}")

class Ikan():
    def __init__(self,alat) -> None:
        self.nafas = alat

    def bernafas(self):
        print(f"Ikan bernafas dengan {self.nafas}")

ayam = Ayam("Paru-paru")
ikan = Ikan("Insang")

ayam.bernafas()
ikan.bernafas()