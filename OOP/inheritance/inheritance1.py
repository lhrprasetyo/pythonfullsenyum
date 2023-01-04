# inheritance --> penurunan sifat
# parent class  
# child class 

class Kucing():#parent class

    def __init__(self):
        self.kelenjar_susu = True
        self.daun_telinga = True

    def makan(self):
        print("kucing makan")
    def minum(self):
        print("kucing minum")

class KucingAnggora (Kucing):#child class
    __jenis_bulu = 'lebat'

    def makan(self):#overriding
        print("kucing anggora makan ")

kucing_anggora = KucingAnggora()
print(kucing_anggora.kelenjar_susu)#mengakses parent class
kucing_anggora.makan()
