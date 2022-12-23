namaL = []
namaP = []
jawab = "ya"
while jawab == "ya" :
    print("---Formulir Pendaftaran kos-kosan---")
    nama = input("Masukkan nama : ")
    jkelamin = input("Jenis kelamin p/l : ")
    if jkelamin == 'l' :
        namaL.append(nama)
    elif jkelamin == 'p':
        namaP.append(nama)
    jawab = input("isi formulir lagi ? ya/tidak ")
print(f"kos putra : {namaL}")
print(f"kos putri : {namaP}")

    
