
class FlowException(Exception):
    pass

class FlowVertex:
    def __init__(self, coordinates, color, dot, adjacencies):
        self.coordinates = coordinates
        self.color = color
        self.dot = dot
        self.adjacencies = adjacencies

    def __str__(self):
        if self.dot:
            return self.color
        if len(self.adjacencies) == 0:
            return ' '
        if len(self.adjacencies) == 1:
            direct = self.direction(self.adjacencies[0])
            if direct == 'N' or direct == 'S':
                return '|'
            return '-'
        direct1 = self.direction(self.adjacencies[0])
        direct2 = self.direction(self.adjacencies[1])
        if ((direct1 == 'N' and direct2 == 'S') or
            (direct1 == 'S' and direct2 == 'N')):
            return '|'
        if ((direct1 == 'N' and direct2 == 'W') or
            (direct1 == 'W' and direct2 == 'N') or
            (direct1 == 'S' and direct2 == 'E') or
            (direct1 == 'E' and direct2 == 'S')):
            return '/'
        if ((direct1 == 'N' and direct2 == 'E') or
            (direct1 == 'E' and direct2 == 'N') or
            (direct1 == 'S' and direct2 == 'W') or
            (direct1 == 'W' and direct2 == 'S')):
            return '\\'
        return '-'

    def connect(self, adjacent):
        self.adjacencies.append(adjacent)
        adjacent.adjacencies.append(self)
        adjacent.color = self.color

    def direction(self, adjacent):
        myrow, mycol = self.coordinates
        adjrow, adjcol = adjacent.coordinates
        if myrow - adjrow > 0:
            return 'N'
        if myrow - adjrow < 0:
            return 'S'
        if mycol - adjcol > 0:
            return 'W'
        return 'E'

class FlowPuzzle:
    def __init__(self, vertices):
        self.vertices = vertices

    def heuristic(self):
        return 1

    def get_vertex(self, coordinates):
        for vertex in self.vertices:
            if vertex.coordinates == coordinates:
                return vertex
        return None

    def __str__(self):
        out = ''
        row = 0
        col = 0
        vertex = self.get_vertex((row, col))
        while vertex:
            out = out + str(vertex)
            col = col + 1
            vertex = self.get_vertex((row, col))
            if vertex is None:
                out = out + '\n'
                row = row + 1
                col = 0
                vertex = self.get_vertex((row, col))
        return out

if __name__ == '__main__':
    v1 = FlowVertex((0, 0), '1', True, [])
    v2 = FlowVertex((0, 1), '1', True, [])
    v3 = FlowVertex((1, 0), None, False, [])
    v4 = FlowVertex((1, 1), None, False, [])
    v1.connect(v3)
    v3.connect(v4)
    v4.connect(v2)
    p1 = FlowPuzzle([v1, v2, v3, v4])
    print(str(p1))
