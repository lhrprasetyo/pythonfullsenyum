# inheritance --> penurunan sifat
# parent class  
# child class 

class Kucing():#parent class

    def __init__(self,berat,warna):
        self.berat = berat
        self.color = warna

    def makan(self):
        print("kucing makan")
    def minum(self):
        print("kucing minum")

    def desc(self):
        print(f"kucing memiliki berat {self.berat}kilogram, dan memiliki warna {self.color}")

class KucingAnggora (Kucing):#child class
    __jenis_bulu = 'lebat'

    def makan(self):#overriding
        print("kucing anggora makan ")

    def desc(self):
        print(f"kucing anggora berbulu {self.__jenis_bulu}, dengan berat {self.berat}, dan memiliki warna {self.color}")

kucing_anggora = KucingAnggora(2.2,'Orange')

kucing2=Kucing(2.5,'hijau')
kucing2.desc()
kucing_anggora.desc()
