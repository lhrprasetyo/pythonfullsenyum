orang = {"nama " : "Sobri"}
umur = {"umur" : 19}
print(orang)
print(umur)

biodata = {
    'nama' : 'sobri',
    'umur' : 20,
    'alamat': 'sayang-sayang',
    'tinggi' : 166.6
}

# mengakses data
print(biodata['nama'])
print()

# menambah data 
biodata['semester'] = 3 
print(biodata)
print()

warnaBuah = dict(jeruk='orange',apel='merah',pisang='kuning')
print(warnaBuah)
print(warnaBuah['jeruk'])
print()

# mengupdate data 
biodata['semester']= 4
print(f"Data berhasil diupdate : {biodata}")
print()

# menghapus data dict 
# 1.menggunakan method pop() -> menghapus data berdasarkan keynya
biodata.pop('semester')
print(f"data dihapus dengan menggunakan method pop() : {biodata}") 
print()
# 2.menggunakan method popitem() -> menghapus item pada data terakhir
biodata.popitem()
print(biodata)

# looping
for b in biodata.values() :
    print(b)
print()

for m,n in biodata.items():
    print (m,n)