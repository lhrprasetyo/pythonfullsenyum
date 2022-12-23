jumlah =[]
items = []
totalBelanja = []
hargaBelanja = []
jawab = "ya"
while jawab == "ya" :
    print("--- Pilih Barang ---")
    print("1. Tomat 1 bungkus : Rp.5000")
    print("2. Ayam 1kg : Rp.45000")
    print("3. Kentang 1kg : Rp.35000")
    print("4. Cabai 1/4kg : Rp.25000")
    print("5. Wortel 1 Bungkus : Rp.7000")
    print()
    belanja = int(input("Mau beli apa ? "))
    jumlahB = int(input("Berapa ? "))
    if belanja == 1 :
        item = "Tomat 1 bungkus"
        harga = 5000
        totalBelanja.append(harga * jumlahB)
        hargaBelanja.append(harga)
        jumlah.append(jumlahB)
        items.append(item)
    elif belanja == 2 :
        item = "Ayam 1kg"
        harga = 45000
        totalBelanja.append(harga * jumlahB)
        hargaBelanja.append(harga)
        jumlah.append(jumlahB)
        items.append(item)
    elif belanja == 3 :
        item = "Kentang 1kg"
        harga = 35000
        totalBelanja.append(harga * jumlahB)
        hargaBelanja.append(harga)
        jumlah.append(jumlahB)
        items.append(item)
    elif belanja == 4 :
        item = "Cabai 1/4kg"
        harga = 25000
        totalBelanja.append(harga * jumlahB)
        hargaBelanja.append(harga)
        jumlah.append(jumlahB)
        items.append(item)
    elif belanja == 5 :
        item = "Wortel 1 bungkus"
        harga = 7000
        totalBelanja.append(harga * jumlahB)
        hargaBelanja.append(harga)
        jumlah.append(jumlahB)
        items.append(item)
    else :
        print("Input yang anda masukkan tidak dikenali")
    jawab = input("Ada lagi ? ya/tidak ")
    print()
print(f"list item : {items}")
print(f"Harga barang barang : {hargaBelanja}")
print(f"Jumlah barang : {jumlah}")
print(f"list harga : {totalBelanja}")
print(f"Total tagihan anda : {sum(totalBelanja)}")



