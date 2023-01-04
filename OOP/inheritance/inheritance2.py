# inheritance --> penurunan sifat
# parent class  
# child class 

class Kucing():#parent class

    def __init__(self):
        self.kelenjar_susu = True
        self.daun_telinga = True
        self.berat = None
        self.warna = None

    def makan(self):
        print("kucing makan")
    def minum(self):
        print("kucing minum")

class KucingAnggora (Kucing):#child class
    __jenis_bulu = 'lebat'

    def makan(self):#overriding
        print("kucing anggora makan ")

    def desc(self):
        print(f"kucing anggora berbulu {self.__jenis_bulu}, dengan berat {self.berat}, dan memiliki warna {self.warna}")

kucing_anggora = KucingAnggora()
kucing_anggora.berat = 2.5
kucing_anggora.warna = 'orange'
kucing_anggora.desc()
