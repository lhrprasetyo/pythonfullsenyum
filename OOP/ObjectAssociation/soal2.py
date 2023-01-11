class Guru():
    def __init__(self,nama,id) -> None:
        self.nama = nama 
        self.id = None

    def pengajar(self) -> str:
        return self.nama

class Hari():
    def __init__(self,hari,pengajar) -> None:
        self.hari =  hari
        self.pengajar = pengajar

    def jadwal(self):
        return self.pengajar.pengajar()

guru1=Guru('budi',1)
guru2=Guru('halim',2)
hari1=Hari('senin',guru2)
print(f'hari  {hari1.hari}, akan diisi oleh pengajar bernama {hari1.jadwal()}')