import random as rand



class Game:
    def __init__(self):
        print("HALLO EVERYONE")

        self.min_room_size = 6
        self.max_room_size = 20
        self.max_rooms = 10
        self.min_rooms = 3
        self.max_iters = 3

        self.map_width = 50
        self.map_height = 50

        self.rooms = []


        self.init_map()
        self.init_rooms()
        self.connect_rooms()

        print(type(self.map))

    def init_map(self):
        for y in range(self.map_height):
            for x in range(self.map_width):
                self.map[x,y] = 0
    
    def init_rooms(self):
        # gens random number for number of rooms in map
        total_rooms = rand.randrange(self.min_rooms, self.max_rooms)


        for i in range(self.max_iters):
            for j in range(total_rooms):
                if len(self.rooms) >= self.max_rooms:
                    break
        
        x = rand.randrange(0, self.map_width)
        y = rand.randrange(0, self.map_height)

        width = rand.randrange(self.min_room_size, self.max_room_size)
        height = rand.randrange(self.min_room_size, self.max_room_size)

        room = Room(x, y, width, height)

        if self.check_for_overlap(room, self.rooms):
            pass
        else:
            self.rooms.append(room)
        
        for room in self.rooms:
            for y in range(room.y, room.y + room.height):
                for x in range(room.x, room.x + room.width):
                    self.map[x,y] = 1
    
    def check_for_overlap(self, room, rooms) -> bool:
        for check_room in rooms:
            room_max_x = room.x + room.width
            room_min_x = room.x

            room_min_y = room.y
            room_max_y = room.y + room.height

            check_min_x = check_room.x
            check_max_x = check_room.x + check_room.width

            check_min_y = check_room.y
            check_max_y = check_room.y + check_room.height

            if ((room_max_x >= check_min_x or room_min_x <= check_max_x) and (room_max_y >= check_min_y or room_min_y <= check_max_y)):
                return True
            else:
                return False
    
    def connect_rooms(self):
        rand.shuffle(self.rooms)
        for i in range(len(self.rooms)-1):
            roomA = self.rooms[i]
            roomB = self.rooms[i+1]
        for x in range(roomA.x,roomB.x):
            self.map[x,roomA.y] = 1
        for y in range(roomA.y, roomB.y):
            self.map[roomA.x,y] = 1
        for x in range(roomB.x,roomA.x):
            self.map[x,roomA.y] = 1
        for y in range(roomB.y, roomA.y):
            self.map[roomA.x,y] = 1
    
    


class Room:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f"A room at ({self.x}, {self.y})"



if __name__ == "__main__":
    root = Game
