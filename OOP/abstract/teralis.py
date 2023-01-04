class Teralis():
    bahan = ''
    ukuran = ''
    harga = None

    def kualitas(self): 
        print('tahan karat hingga 10 tahun')

    def __init__(self,bahan,ukuran,harga) -> None:
        self.bahan = bahan
        self.ukuran = ukuran
        self.harga = harga

    def __repr__(self):
        return (f"Bahan : {self.bahan} | Ukuran : {self.ukuran} | Harga : {self.harga}")
        
    def desc(self):
        print(f"{self.bahan} | {self.ukuran} | {self.harga}")
# # objek1
# teralis = Teralis()
# teralis.bahan = 'baja'
# teralis.ukuran = '158.4cm x 80cm'

# print("Teralis 1 :")
# print(f"Bahan  :  {teralis.bahan}")
# print(f"ukuran :  {teralis.ukuran}")
# teralis.kualitas()

teralis1=Teralis('plat','190cm x 83.6cm',235000)
teralis1.desc()
print(teralis1)
