# import, untuk ambil modul 
import segitiga 
# kalau mau cara lebih spesifik : 
from persegi import persegiPanjang,persegi
# alternatif kalau mau manggil tanpa nulis nama modul :
from layanglayang import *

# bisa langsung print var dari modul , asal nulis nama modul di depannya
print(segitiga.test)

keliling_segitiga = segitiga.ksegitiga(12,1,3)

# buat_var_dlu, trus import pake nama_modul.function
print(f"keliling segitia : {keliling_segitiga}")

print(F"keliling persegi : {persegi(4)}")

# print tanpa menggunakan modul 
print(layang(1,8,3,9))
