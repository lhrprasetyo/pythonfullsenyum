class Ayam():
    makanan = None
    def makan(self):
        return f"{self.makanan}"
class Kucing():
    makanan = None
    def makan(self):
        return f"{self.makanan}"
    
kucingOren = Kucing()
kucingOren.makanan = 'ikan cupang'

ayamKatek = Ayam()
ayamKatek.makanan = 'nasi'

ayamKatek.makan()
for a in [ayamKatek,kucingOren]:
    print(a.makan())