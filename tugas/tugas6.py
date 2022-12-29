biodata = {
    'nama':'Randi',
    'alamat':{
        'alamat':'jln. Belibis',
        'kecamatan':'Pejanggik',
        'kota':'Mataram',
        'Provinsi':'NTB'
    },
    'nilai_raport':[87,75,85,90]
}

# 1.Akses value pada variable biodata dengan key nama
print(f"1.Nama : {biodata['nama']}")
# 2.Akses value kecamatan pada variable biodata 
print(f"2.Alamat : {biodata['alamat']['kecamatan']}")
# 3.tambah key dan value pada variabel biodata dengan key hobi dan value bebas
biodata['hobi']='Belajar'
print(f"3.Hobi : {biodata['hobi']}")
# 4.ubahlah value pada key nama pada variabel biodata 
biodata['nama']= 'Dani'
print(f"4. {biodata['nama']}")
# 5.Hapus data dengan key provinsi pada variabel biodata 
biodata['alamat'].pop('Provinsi')
print(f"5. {biodata}")