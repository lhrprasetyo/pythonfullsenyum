jawab = "ya"
while (jawab == "ya"):
    lampu = input("Masukkan warna lampu : ")
    if (lampu == "merah"):
       print("berhenti mas") 
    elif (lampu == "hijau"):
       print("gas bor")
    elif(lampu == "kuning"):
        print("hati hati")
    elif(lampu == "sampai"):
        print("siap")
        break     
    jawab = input("lanjut ? ")