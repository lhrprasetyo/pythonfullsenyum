class Kuda():
    nama = ''
    jenis = ''
    harga = None

    def makanan(self):
        print('kuda dari peternakan kami diberi pakan dengan makanan yang berkualitas ')
    
    def __init__(self,nama,jenis,harga) -> None:
        self.nama = nama
        self.jenis = jenis
        self.harga= harga
        
    def __repr__(self):
        return (f"Nama Kuda : {self.nama} | Jenis Kuda : {self.jenis} | Harga : {self.harga}")
        
    def desc(self):
        print(f"{self.nama} | {self.jenis} | {self.harga}")


# # objek1
# kuda = Kuda()
# kuda.nama = "grace's secret"
# kuda.jenis = "kuda liar"
# kuda.harga = 999999999


# print(f"Nama kuda : {kuda.nama}")
# print(f"Jenis kuda : {kuda.jenis}")
# print(f"Penawaran tertinggi sementara : {kuda.harga}")
# kuda.makanan()

kuda1 = Kuda('LF','unicorn',100000000)
kuda1.desc()
print(kuda1)