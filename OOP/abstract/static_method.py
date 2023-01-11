# static method merupakan fungsi atau method yang bersifat statis dalam sebuah class 

# cara membuat static method 
#  dengan cara mendefinisikan decorator @staticmethod pada fungsi  yang ingin dibuat menjadi statis

class Konversi:

    @staticmethod
    def satuan_ke_lusin(n):
        return n/12
    
    @staticmethod
    def satuan_ke_kodi(n):
        return n/20
    
    @staticmethod
    def satuan_ke_rim(n):
        return n/500

k = Konversi.satuan_ke_lusin(22)
kd = Konversi.satuan_ke_kodi(22)
r = Konversi.satuan_ke_rim(500)
print(k)
print(r)
print(kd)

class Mahasiswa:
    def __init__(self,nama) -> None:
        self.nama = nama
    
    def getNama(self):
        return self.nama

    @staticmethod
    def hurufBesar(nama):
        return nama.upper()

d = Mahasiswa(input("nama mahasiswa : "))
print(d.hurufBesar(d.getNama()))