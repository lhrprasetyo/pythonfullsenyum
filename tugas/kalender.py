print("Masukkan bukan sesuai format berikut : ")
print("1.Januari    2.Februari      3.Maret     4.April")
print("5.Mei        6.Juni          7.Juli      8.Agustus   9.September")
print("10.Oktober   11.November     12.Desember")

bulan =int( input("Masukkan bulan : "))
tanggal =int( input("Masukkan tanggal : "))

if bulan == 1:
    if tanggal>=1 and tanggal <=4:
        print("Jumadil ula 1443")
    elif tanggal >4 and tanggal <=31:
        print("Jumadil akhir 1443")
# bulan ke 2
elif bulan == 2:
    if tanggal == 1:
        print("Jumadil akhir 1443")
    elif tanggal >=2 and tanggal <=28:
        print("Rajab 1443")
# bulan ke 3
elif bulan == 3:
    if tanggal>=1 and tanggal <=3:
        print("Rajab 1443")
    elif tanggal >=4 and tanggal <=31:
        print("Sya'ban 1443")
# bulan ke 4
elif bulan == 4 :
    if tanggal == 1 or tanggal == 2 :
        print("Sya'ban 1443")
    elif tanggal >= 3 and tanggal <=30 :
        print ("Ramadhan 1443")
# bulan ke 5
elif bulan == 5 :
    if tanggal == 1 :
        print("Ramadhan 1443")
    elif tanggal >= 2 and tanggal <=31 :
        print ("Syawwal 1443")
# bulan ke 6
elif bulan == 6 :
    if tanggal == 1 and tanggal <= 29 :
        print("Dzulqaidah 1443")
    elif tanggal ==30 :
        print ("Dzulhijjah 1443")
# bulan ke 7
elif bulan == 7 :
    if tanggal >=1 and tanggal <=29 :
        print("Dzulhijjah 1443")
    elif tanggal == 30 or tanggal == 31 :
        print ("Muharram 1443")
# bulan ke 8
elif bulan == 8 :
    if tanggal >= 1 and tanggal <= 28 :
        print("Muharram 1443")
    elif tanggal >= 29 and tanggal <=31 :
        print ("Shafar 1443")
# bulan ke 9
elif bulan == 9 :
    if tanggal >= 1 and tanggal <= 26 :
        print("Shafar 1443")
    elif tanggal >= 27 and tanggal <=30 :
        print ("Rabi'ul Awwal 1443")
# bulan ke 10
elif bulan == 10 :
    if tanggal >= 1 and tanggal <= 26 :
        print("Rabi'ul Awwal 1443")
    elif tanggal >= 27 and tanggal <=31 :
        print ("Rabi'ul Akhir 1443")
# bulan ke 11
elif bulan == 11 :
    if tanggal >= 1 and tanggal <= 24 :
        print("Rabi'ul Akhir 1443")
    elif tanggal >= 25 and tanggal <=30 :
        print ("Jumadal ula 1443")
# bulan ke 12
elif bulan == 12 :
    if tanggal >= 1 and tanggal <= 24 :
        print("Jumadal ula 1443")
    elif tanggal >= 25 and tanggal <=31 :
        print ("Jumadal Akhiroh 1443")
else :
    print("maaf, masukkan jumlah bulan yang valid")
print("---------------")