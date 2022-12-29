# memahami string sebagai array
nama ='Luhur Budi Prasetyo'
print(f"Akses huruf L : {nama[0]}")

# melakukan looping
for n in nama :
    print(n)

# mengecek panjang dari string 
print(f"Panjang string pada var nama : {len(nama)}")

# check string 
print("Budi" in nama)

# check is  not 
print("budi" not in nama)

# slicing string / mengiris string 
print(f"{nama[:11]}")

# slice to the end
print(f"{nama[6:]}")
