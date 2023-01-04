class Paus():
    umur = None
    berat = None
    makanan = []

    def __init__(self,umur,berat):
        self.umur = umur
        self.berat = berat

    def __repr__(self):
        return str(self.umur)

    def berenang(self):
        print("mampu berenang selama 3 hari 3 malam tanpa beristirahat")

    def makan(self,objek):
        objek =self.makanan.append(objek)
        print(f"paus berhasil memangsa {self.makanan}")
        
        
    def makanan_hari_ini(self):
        print(f"Makanan yang sudah dimakan paus adalah :{self.makanan}")

class Cumi():
    nomor : None

    def __init__(self,nomor):
        self.nomor = nomor

    def __repr__(self):
        return self.nomor

    def makan(self):
        print("plankton")

class Plankton():
    nomor = None

    def __init__(self,nomor):
        self.nomor = nomor

    def __repr__(self):
        return self.nomor

    def makan(self):
        print("makan plankton yang lebih kecil")

class Krill():
    nomor = None

    def __init__(self,nomor):
        self.nomor = nomor

    def __repr__(self):
        return self.nomor
        
    def makanan():
        print("makan tumbuhan dan hewan mikroskopik")

paus = Paus(9,"500Kg")
paus.makanan =[]
print(paus)

cumi1 = Cumi('cumi1')
cumi2 = Cumi('cumi2')
cumi3 = Cumi('cumi3')
plankton1 = Plankton('pl1')
plankton2 = Plankton('pl2')
plankton3 = Plankton('pl3')
krill1 = Krill('kr1')
krill2 = Krill('kr2')
krill3 = Krill('kr3')

paus.makan(cumi1)
paus.makanan_hari_ini()
paus.makan(cumi3)
paus.makanan_hari_ini()