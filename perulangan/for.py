# counted loop
# for i in range(10):
#     # code di dalam loop 
#     print(f"Perulangan ke {i}")
# code di luar loop

# for  i in range(100):
#     print("ambil gelas plastik")
#     print("tuang okky jelly ke dalam gelas hingga penuh")
#     print("tutup okky jelly drink")
#     print(f"Kemasan ke {i}\n")

# mengurai array
makanan = ["bakwan","perkedel","mendoan"]
for i in makanan:
    print(i)

# mengurai string 
nama = "Budi"
for n in nama:
    print(n)

# untuk mengecek array
makanan = ["bakwan","perkedel","mendoan"]
for i in makanan:
    if i == "bakwan":
        print("Bakwannya ada")
        break
    else :
        print("Bakwannya habis")

# perulangan untuk melwati sebuah statement, atau peggunaan continue
for i in range(10):
    if i == 8:
        continue
    print(i)

print(10*"---")

# for using start parameter
for i in range (2,18):
    print(i)

print(10*"---")
# ini angka pertama untuk angka pertamanya, angka kedua untuk batas ujung nya, angka ketiga kelipatannya+
for i in range (0,100,12):
    print (i)

for i in range(10):
    if i == 8:
        pass
    print(i)

print(10*"---")