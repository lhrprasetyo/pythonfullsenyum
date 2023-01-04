class Manusia():
    nama = ''
    __gender = None
    usia = None

    def makan (self):
        print("Manusia makan nasi goreng")
    
    def minum(self):
        ...
    
    def main(self):
        print("Manusia gemar bermain")

    def set_gender (self,gender):
        self.__gender = gender
    
    def get_gender(self):
        return self.__gender

    def ulang_tahun(self):
        self.usia = self.usia +1

# instance object 
manusia = Manusia() #object1
manusia1 = Manusia() #object2

print(f"ketika attribut nama pada manusia masih kosong, maka nama  : {manusia1.nama}")

# akses manusia 
manusia.nama = "budi"
manusia.gender = "laki-laki"
manusia.usia = 20

print(f"mengakses attribut nama dari object manusia : {manusia.nama}")
print(f"mengakses attribut gender dari object manusia : {manusia.gender}")
print(f"mengakses attribut usia dari object manusia : {manusia.usia}")

print   (f"usia sebelum ulang tahun : {manusia.usia}")
manusia.ulang_tahun()
print   (f"usia sesudah ulang tahun : {manusia.usia}")

# mengakses method 
manusia.makan()