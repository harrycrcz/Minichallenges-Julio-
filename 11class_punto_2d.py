class Punto2D:
    def __init__(self, x, y, files, columns):
        self.x = x
        self.y = y
        self.files = files
        self.columns = columns
        self.map = [[' ' for _ in range(self.columns)]
                    for _ in range(self.files)]

    def coordenadas(self):
        self.map[self.x][self.y] = 'C'
        return self.map


files_map = 10
columns_map = 10
punto_x = 2
punto_y = 3

map = Punto2D(punto_x, punto_y, files_map, columns_map)
print(map.coordenadas())
