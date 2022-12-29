# function 
def hello():
    print("Hello world")
hello()

def perkenalan(nama):
    print(f"halo, nama saya {nama}")

perkenalan("Sobri")
perkenalan("Budi")
perkenalan("Afif")

def perkalian(x,y):
    jumlah = x*y
    print(f"hasil dari {x}*{y} = {jumlah}")
perkalian(14,2)

def biodata(namaDepan,namaBelakang,umur):
    print(f"Nama saya {namaDepan} {namaBelakang}, dan saya berumur {umur} tahun")

biodata("Budi", "Prasetyo", 20)