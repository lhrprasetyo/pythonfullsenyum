class Mamalia():
    def __init__(self) -> None:
        self.kelenjar_susu = True
        self.bulu =  True
        self.alat_pernapasan = None

    def berkembang_biak(self):
        print('berkembang biak dengan cara melahirkan')
    def menyusui(self):
        print("mamalia menyusui")
    
class Paus(Mamalia):
    def __init__(self) :
        self.jenis_makanan = None
        self.jenis_paus= None

    def berenang(self):
        print('paus berenang kan')
    def makan(self):
        print('paus makan plankton')
    def desc(self):
        print(f"paus {paus.jenis_paus} bernapas dengan {paus.alat_pernapasan},dan memakan {paus.jenis_makanan}")


class Kuda(Mamalia):
    def __init__(self) :
        self.jenis_makanan = None
        self.warna= None

    def berjalan(self):
        print('sudah pasti kuda berjalan')
    def makan(self):
        print('kuda makan rumput')
    def desc(self):
        print(f"kuda makan {self.jenis_makanan}, dan berwarna {self.warna}")


class Sapi(Mamalia):
    def __init__(self) :
        self.jenis = None
    
    def makan(self):
        print("sapi makan rumput")
    def desc(self):
        print(f"jenis sapi ini adalah {self.jenis}")

# paus 
paus = Paus()
paus.jenis_makanan = 'plankton'
paus.jenis_paus = 'orca'
paus.alat_pernapasan = 'paru-paru'
paus.desc()
print()

# kuda 
kuda = Kuda()
kuda.jenis_makanan = 'rumput'
kuda.warna = 'hitam'
kuda.desc()
print()

# sapi
sapi = Sapi()
sapi.jenis = 'sapi perah'
sapi.desc()
print()