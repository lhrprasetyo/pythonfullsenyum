# chaining method (method berantai)

class Warteg():
    def __init__(self) :
        self.total = 0
        self.item = []
    
    def nasi(self):
        self.item.append("nasi 1 porsi")
        self.total+3000
        return self

    def bakwan(self):
        self.item.append("bakwan")
        self.total = self.total+2000
        return self

    def kangkung(self):
        self.item.append("kangkung")
        self.total = self.total+1500
        return self

    def ayam(self):
        self.item.append("ayam 1")
        self.total = self.total+8000
        return self

    def krupuk(self):
        self.item.append("krupuk")
        self.total = self.total+3000
        return self

    def bayar(self):
        print(f"Item : {self.item}")
        print(f"Total : {self.total}")
        return self

abang = Warteg().nasi().bakwan().kangkung().krupuk().bayar()