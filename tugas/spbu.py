print("-------Selamat datang di SPBU-------")
pertamax=15000
ptrb=17000
pplus=10000
plite=12000
pdex=13000
dexlt=10000
slr=8000
print(f"1.Pertamax = Rp. {pertamax}")
print(f"2.Pertamax turbo = Rp. {ptrb}")
print(f"3.Pertamax Plus = Rp. {pplus}")
print(f"4.Pertalite = Rp. {plite}")
print(f"5.Pertamina Dex = Rp. {pdex}")
print(f"6.Dexlite  = Rp. {dexlt}")
print(f"7.Solar = Rp. {slr}")
print()
print("Pilih bahan bakar")
bbm = int(input("masukkan jenis bahan bakar : "))
jumlah = float(input("Masukkan jumlah bahan bakar : "))
if bbm == 1 :
    print(f"total bayar : Rp. {pertamax * jumlah}")
elif bbm == 2 :    
    print(f"total bayar : Rp. {ptrb * jumlah}")
elif bbm == 3 :    
    print(f"total bayar : Rp. {pplus * jumlah}")
elif bbm == 4 :    
    print(f"total bayar : Rp. {plite * jumlah}")
elif bbm == 5 :    
    print(f"total bayar : Rp. {pdex * jumlah}")
elif bbm == 6 :    
    print(f"total bayar : Rp. {dexlt * jumlah}")
elif bbm == 7 :    
    print(f"total bayar : Rp. {solar * jumlah}")
else :
    print("Perintah tidak diketahui")

    
