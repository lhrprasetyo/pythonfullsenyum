tagihan = int(input("Masukkan jumlah tagihan : Rp."))
print("----------------")
if tagihan>100000:
    disc = 5*tagihan/100
    print("Selamat, anda mendapatkan diskon 5%!")
    print(f"Harga asli : {tagihan}")
    print(f"Harga Tagihan : {tagihan-disc}")
else :
    print(f"Harga tagihan = {tagihan}")
print("----------------")
