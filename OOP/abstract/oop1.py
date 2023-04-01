class Manusia():
    __nama = '' #public attribute
    __gender = None
    __usia = None


    def atur_nama(self,nama):
        self.__nama = nama

    def atur_usia(self,usia):
        self.__usia = usia

    def ambil_nama(self):
        return self.__nama
    
    def ambil_usia(self):
        return self.__usia

    def set_gender (self,gender):
        self.__gender = gender
    
    def get_gender(self):
        return self.__gender

    def ulang_tahun(self):
        self.usia = self.usia +1

    def desc(self):
        print(f"nama : {self.__nama}, gender : {self.__gender},umur : {self.__usia},")

# instance object / cetak objek
manusia = Manusia() #object1
manusia1 = Manusia() #object2

# print(f"ketika attribut nama pada manusia masih kosong, maka nama  : {manusia1.nama}")

# akses manusia 
manusia.atur_nama("budi") 
# manusia.__gender = 'laki'
manusia.set_gender("laki-laki") 
manusia.atur_usia(20)

manusia.desc()

# print(f"mengakses attribut nama dari object manusia : {manusia.nama}")
# print(f"mengakses attribut gender dari object manusia : {manusia.get_gender()}")
# print(f"mengakses attribut usia dari object manusia : {manusia.usia}")

# print(f"nama manusia 1:{manusia1.nama}")
# manusia1.nama = "sobri"
# print(f"nama manusia 1:{manusia1.nama}")


# print   (f"usia sebelum ulang tahun : {manusia.usia}")
# manusia.ulang_tahun()
# print   (f"usia sesudah ulang tahun : {manusia.usia}")

# # mengakses method 
# manusia.makan()