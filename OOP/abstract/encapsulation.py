
class Manusia():
    nama = None #private attribute
    gender = None

    def nama(self):
        return f"{self.nama}"
    
    def description(self):
        print (f"nama :{self.nama} gender :{self.gender}")
    
manusia1 = Manusia()

manusia1.nama = 'BUDI'
manusia1.gender = 'Pria'
manusia1.description()