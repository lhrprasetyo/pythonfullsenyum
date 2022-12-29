def test(*args):
    print(args)
    print(args[0]+7)
    print(args[1])
test(8,1, 'hola')

def penjumlahan(*args):
    total = sum(args)
    print(total)

penjumlahan(8,2,1,5,4)


def penjumlahan(*args):
    total = args[0]+args[1]
    return total

print(penjumlahan(1,2))