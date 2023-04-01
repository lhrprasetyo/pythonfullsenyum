class Manusia():
    nama = None

    def makan(self):
        pass
    
    def __repr__(self) -> str:
        return self.nama

manusia1 = Manusia()
manusia1.nama = 'sobri'

print(manusia1.nama)
print(manusia1)