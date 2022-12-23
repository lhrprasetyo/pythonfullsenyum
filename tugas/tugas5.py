barang1 = {
    'kode' : 1,
    'namaBarang' : 'Close up',
    'harga' : 15000
}
barang2 = {
    'kode' : 2,
    'namaBarang' : 'Close down',
    'harga' : 15000
}

listBarang = {
    'kode' : [1,2,3],
    'namaBarang' : ['Close Up','Dettol','Clear'],
    'hargaBarang' : [10000,15000,20000]
}
barang=[barang1,barang2]
barang[0]['harga'] = 17500
barang[1]['harga'] = 17500
print(barang)
print()

listBarang['kode'].append(4)
listBarang['namaBarang'].append('handyplast')
listBarang['hargaBarang'].append(12500)
print(listBarang)
print()

listBarang['kode'].remove(2)
listBarang['namaBarang'].remove('Dettol')
listBarang['hargaBarang'].remove(15000)
print(listBarang)

# kalau ada array, pakein append untuk update data, wajib