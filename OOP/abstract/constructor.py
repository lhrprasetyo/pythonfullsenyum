# __init__ --> merupakan method yang pertama kali akan di eksekusi ketika kita menginstance sebuah object 

class Paus():
    nama = None
    umur = None
    jenis = None
    harga = None

    def __init__(self,name,age,type,price):
        self.nama = name
        self.umur = age
        self.jenis = type
        self.harga = price


    def deskripsi(self):
        print(f"{self.nama} | {self.umur} | {self.jenis} | {self.harga}")

    def __repr__(self):
        return self.nama

class Penguin():
    def __init__(self):
        print("ini adalah penguin :D")

class Kuda():
    def __init__(self):
        pass

paus = Paus('Jen',99,'orCA',99999999)
print(paus.nama)
paus.deskripsi()

print(paus)
