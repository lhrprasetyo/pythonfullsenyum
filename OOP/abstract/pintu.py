class Pintu():
    model = None
    bahan = None
    harga = None

    def fleksibilitas(self):
        print('wajib bisa dibuka keluar dan ke dalam')

    def __init__(self,model,bahan,harga):
        self.model = model 
        self.bahan = bahan 
        self.harga = harga
    
    def __repr__(self):
        return (f"kami membuat pintu dengan model {self.model} menggunakan bahan {self.bahan}, yang pastinya murah, dengan harga {self.harga} ")
        
    def desc(self):
        print(f"{self.model} | {self.bahan} | {self.harga}")


# # objek1
# pintu = Pintu()
# pintu.model = 'model persegi panjang dan setengah lingkaran dengan kotak-kotak seperti jendela di tengahnya '
# pintu.bahan = 'kayu jati'

# print("Pintu 1 :")
# print(f"Model   : {pintu.model}")
# print(f"bahan   : {pintu.bahan}")
# pintu.fleksibilitas()

print()
# objek 2
pintu2 = Pintu('model persegi panjang dengan motif ukiran bunga di tengah','kayu sengon',800000)
pintu2.desc()
print(pintu2)
