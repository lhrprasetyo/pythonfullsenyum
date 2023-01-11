class Serigala():
    def __init__(self,nomor,jenis,umur,daya_gigit,hp) -> None:
        self.id = nomor
        self.jenis = jenis
        self.umur = umur    
        self.daya_gigit = daya_gigit
        self.hp = hp

    def menyerang(self,mangsa):
        mangsa.hp -= self.daya_gigit
        print(f'{self.id} menyerang {mangsa.id}')

    def berlari(self):
        print(f"{self.id} berlari")
        
    def deskripsi(self):
        if(self.hp <0):
            print(f"{self.id} died")
        else:
            print(f"{self.id} memiliki hp {self.hp}")

class Kelinci():
    def __init__(self,nomor,hp,warna) -> None:
        self.id = nomor
        self.hp = hp
        self.warna = warna

    def makan(self):
        print(f"{self.id} makan")

    def berlari(self):
        print(f"{self.id} berlari")

    def bersembunyi(self):
        print(f"{self.id} bersembunyi")

    def deskripsi(self):
        if(self.hp <0):
            print(f"{self.id} died")
        else:
            print(f"{self.id} memiliki hp {self.hp}")

s1 = Serigala('serigala 1','Alaska',2.5,14,100)
s2 = Serigala('serigala 2','Gurun',1.5,25,80)
k1 = Kelinci('kelinci 1',10,'putih')
        
s1.menyerang(k1)
k1.deskripsi()

s2.menyerang(s1)
s1.deskripsi()
s2.menyerang(s2)
s2.deskripsi()
