import random as rand



class Game:
    def __init__(self):
        print("HALLO EVERYONE")

        self.min_rooms = 2
        self.max_rooms = 6
        self.max_room_size = 20
        self.min_room_size = 3

        self.map_width = 50
        self.map_height = 50

        self.max_iters = 3

        self.map = [[0 for i in range(self.map_width)] for j in range(self.map_height)]

        self.rooms = []

        self.create_rooms()
        self.connect_rooms()

        self.print_map()

    def create_rooms(self):
        for j in range(0, self.max_iters):
            if (len(self.rooms) >= self.max_rooms):
                break
            num_rooms = rand.randint(self.min_rooms, self.max_rooms)

            for i in range(num_rooms):
                height = rand.randint(self.min_room_size, self.max_room_size)
                width = rand.randint(self.min_room_size, self.max_room_size)

                room = Room(rand.randint(0, self.map_width - width), rand.randint(0, self.map_height - height), width, height)

                if self.check_overlap(room):
                    pass
                else:
                    self.rooms.append(room)
            
            for room in self.rooms:
                for x in range(room.x, room.x + room.width):
                    for y in range(room.y, room.y + room.height):
                        self.map[y][x] = 1

    def print_map(self):
        for x in range(0, self.map_width):
            for y in range(0, self.map_height):
                if self.map[x][y] == 1:
                    print(' ', end='')
                    print(' ', end='')
                else:
                    print('x', end='')
                    print(' ', end='')
            print()
    
    def check_overlap(self, croom):
        for room in self.rooms:
            croom_min_x = croom.x
            croom_max_x = croom.x + croom.width

            croom_min_y = croom.y
            croom_max_y = croom.y + croom.height

            room_min_x = room.x
            room_max_x = room.x + room.width

            room_min_y = room.y
            room_max_y = room.y + room.height

            if ((croom_min_x <= room_max_x and croom_max_x >= room_min_x) and (croom_min_y <= room_max_y and croom_max_y >= room_min_y)):
                return True
            else:
                return False
        
    def connect_rooms(self):
        rand.shuffle(self.rooms)

        for i in range(len(self.rooms) - 1):
            roomA = self.rooms[i]
            roomB = self.rooms[i + 1]

            for x in range(roomA.x, roomB.x):
                self.map[x][roomA.y] = 1
            for y in range(roomA.y, roomB.y):
                self.map[roomA.x][y] = 1
            
            for x in range(roomB.x, roomA.x):
                self.map[x][roomA.y] = 1
            for y in range(roomB.y, roomA.y):
                self.map[roomA.x][y]

    
    
class Room:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f"A room at ({self.x}, {self.y})"



if __name__ == "__main__":
    root = Game()
