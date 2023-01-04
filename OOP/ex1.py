class Siswabaru():
    nama = ''
    __usia = 8

    def set_usia(self,usia):
        self.__usia = usia

    def get_usia(self):
        return self.__usia

siswa1 = Siswabaru()
siswa1.nama = 'Luhur Budi Prasetyo'
usia1 = siswa1.get_usia() +1

print(f"Nama : {siswa1.nama}")
print(f"usia : {usia1}")