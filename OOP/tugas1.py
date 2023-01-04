class Pintu():
    model = ''
    bahan = ''
    harga = None

    def fleksibilitas(self):
        print('wajib bisa dibuka keluar dan ke dalam')

class Teralis():
    bahan = ''
    ukuran = ''
    harga = None

    def kualitas(self): 
        print('tahan karat hingga 10 tahun')

class Kuda():
    nama = ''
    jenis = ''
    harga = None

    def makanan(self):
        print('kuda dari peternakan kami diberi pakan dengan makanan yang berkualitas ')

# objek1
pintu = Pintu()
pintu.model = 'model persegi panjang dan setengah lingkaran dengan kotak-kotak seperti jendela di tengahnya '
pintu.bahan = 'kayu jati'

print("Pintu 1 :")
print(f"Model   : {pintu.model}")
print(f"bahan   : {pintu.bahan}")
pintu.fleksibilitas()

print()
# objek2
teralis = Teralis()
teralis.bahan = 'baja'
teralis.ukuran = '158.4cm x 80cm'

print("Teralis 1 :")
print(f"Bahan  :  {teralis.bahan}")
print(f"ukuran :  {teralis.ukuran}")
teralis.kualitas()

print()
# objek3
kuda = Kuda()
kuda.nama = "grace's secret"
kuda.jenis = "kuda liar"
kuda.harga = 999999999


print(f"Nama kuda : {kuda.nama}")
print(f"Jenis kuda : {kuda.jenis}")
print(f"Penawaran tertinggi sementara : {kuda.harga}")
kuda.makanan()
