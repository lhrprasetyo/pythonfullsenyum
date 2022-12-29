def test(**kwargs):
    print(kwargs)
    print(kwargs['nama'])

test(nama='budi',alamat='labuapi')

def penjumlahan(**kwargs):
    total = kwargs['x']+kwargs['y']
    return total

print(penjumlahan(x=10,y=3))