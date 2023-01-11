class Kampus():
    nama = None
    fakultas = []
    def __repr__(self) -> str:
        return self.nama

    def tambah_fakultas(self,fakultas):
        self.fakultas.append(fakultas)

    def hapus_fakultas(self,fakultas):
        self.fakultas.remove(fakultas)

    def list_fakultas(self):
        print(f"pada kampus {self.nama} terdapat beberapa fakultas diantaranya : {self.fakultas}")
        
    
class Fakultas():
    def __init__(self,nama) -> None:
        self.nama = nama

    def __repr__(self) -> str:
        return self.nama

k1 = Kampus()
k1.nama = 'UNRAM'

f1 = Fakultas('kedokteran')
f2 = Fakultas('teknik')
f3 = Fakultas('hukum')

k1.tambah_fakultas(f1)
k1.tambah_fakultas(f2)
k1.tambah_fakultas(f3)

k1.list_fakultas()