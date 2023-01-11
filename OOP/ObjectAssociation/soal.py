class  Sapi():
    def __init__(self,jenis,meminum):
        self.jenis = jenis
        self.meminum = meminum
        self.batas = 100

    def minum(self,objek):
        objek.isi -= self.meminum 
        print(f'sapi telah meminum {self.meminum} liter air')
        
class Ember():
    def __init__(self,ember,isi):
        self.nama = ember
        self.isi = isi

    def desc(self):
        print(f"Jumlah air saat ini :  {self.isi}")


s1 = Sapi('desa',5)
a1 = Ember('Ember 1',100)

s1.minum(a1)
a1.desc()