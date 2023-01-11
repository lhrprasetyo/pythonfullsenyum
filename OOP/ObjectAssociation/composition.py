class Building():
    name = None
    room = []

    def __repr__(self) -> str:
        return self.name

    def create_room(self,room):
        self.room.append(room)

    def remove_room(self,room):
        self.room.remove(room)

    def list_room(self):
        print(f"ruangan dalam bangunan {self.name} : {self.room}")

class Room():
    name = None
    color = None

    def __repr__(self) -> str:
        return self.name

rumah = Building()
rumah.name = "Itu"

ruangan1 = Room()
ruangan1.name = 'internet'
ruangan1.color = 'blue'

ruangan2 = Room()
ruangan2.name = 'makan'
ruangan2.color = 'white'

ruangan3 = Room()
ruangan3.name = 'belajar'
ruangan3.color = 'brown'

print(f'Ruangan dalam rumah  {rumah} : {rumah.room}')

rumah.create_room(ruangan1)
rumah.create_room(ruangan3)
rumah.create_room(ruangan2)

rumah.list_room()

rumah.remove_room(ruangan3)
rumah.list_room()