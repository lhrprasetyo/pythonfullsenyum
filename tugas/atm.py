jawab = "ya"
trial = 0
while jawab == "ya": 
        pin1= int(input("Masukkan pin anda : "))
        if pin1 == 123456:
            print("Silahkan masuk ke menu selanjutnya")
            break
        else :
            trial +=1
            jawab = input(f"Pin salah, Coba lagi? ya/tidak (percobaan ke {trial}) ")
            if trial ==3 :
                print ("Anda telah mencoba sebanyak 3 kali, maaf kartu anda tertelan")
                break
            else :
                print("Kartu anda keluar")
    