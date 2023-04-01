import copy


campur = ["sobri",12,True,3.14]
print(f"list : {campur}")
print()

film =["Naruto","One Piece","Avenger","Fast and Furious","Pengabdi Setan"]
print(f"List Film : {film}")
print()

# mengambil data pada index tertentu
print(f"Ambil data pada index ke 0 : {film[0]}")
print(f"Ambil data pada index ke 3 : {film[3]}")
print()

# mengambil data pada index 1 sampai 3
print(f"Ambil data pada index 1 sampai 3 : {film [1:4]}")
print()

# megambil data sebelum dan sampai index ke 3
print(f"Mengambil data sebelum dan sampai index 3 : {film[:4]}")
print()

# megambil data dari index ke 3 sampai terakhir :
print(f"Mengambil data dari index ke 3 sampai terakhir : {film[3:]}")
print()

# menghitung jumlah data pada sebuah array :
jumlah = 0
for i in film :
    jumlah +=1
    print (f"Jumlah data : {jumlah}")
    print()
print()
# atau sintax yang lebih singkatnya :
print(f"Jumlah film : {len((film))}")
print()

# mengecek ketersediaan data pada sebuah array
print("Avenger" in film)
print("MikeyMouse" in film)
print()

# menambahkan data pada array
# 1.menggukan method append():
film_baru = "Avatar 2"
film.append(film_baru)
print(f"Film berhasil diupdate : {film}")
print()

# 2.Menggunakan method insert():
film_baru2 = "Korin"
film.insert(2,film_baru2)
print(f"Film berhasil diupdate : {film}")
print()

# mengubah data:
film_baru3 = "Kupu-kupu malam"
film[5] = film_baru3
print(f"Film berhasil diupdate : {film}")

# menghapus data pada array :
# 1.menggunakan method pop()
film.pop()
print(f"Film berhasil dihapus {film}")
print()

# 2.menggunakan method remove()
film.remove("Avenger")
print(f"Film berhasil dihapus {film}")
print()

# 3.menggunakan method clear
# film.clear()
# print(f"Film berhasil dihapus : {film}")

# mengurutkan data pada array menggunakan method sort()
angka = [1,3,5,4,2,9,8,6,7]
film.sort()
angka.sort(reverse=True)
print(f"Angka berhasil diurutkan menjadi : {angka}")
print(f"film berhasil diurutkan : {film}")
print()

# Membalik data menggunakan reverse
buah = ['ceri','nanas','jeruk','anggur','pisang','jeruk']
buah.reverse()
print(f"membalik buah dari kanan ke kiri : {buah}")
print()

# menghitung jumlah item yang sama menggunakan method count
print(f"Jumlah jeruk : {buah.count('jeruk')}")
print()

# copy isi variabel
buah_buahan = buah.copy()
print(f"Buah - buahan : {buah_buahan}")
print()

# array di dalam array 
matrix = [
    [1,2,3,4,5,6],
    [7,8,9,10,11],
    [12,13,14,15,16]
]
print(matrix[1][3])
matrix[1][4] = 20
print(f"Matrix baru : {matrix}")


# bonus materi :
mylist = [1,2,3,4,5]
myCopy = list(mylist)
# or
mycops = mylist[:]

# tricks for new list:

secondList = [i*i for i in mylist]

mylist.append(6)
print (f"Ini merupakan list awal {mylist}")
print()
print (f"Ini merupakan list copy metode 1 {myCopy}")
print()
print (f"Ini merupakan list copy metode 2 {mycops}")
print()
print(f"membuat list menggunakna loop(jadi pangkat 2 atau dikalikan dengan diri sendiri sesuai kebutuhan){secondList}")