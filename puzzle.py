
class FlowException(Exception):
    pass

class FlowPuzzle:
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

    def __init__(self, vertices):
        self.vertices = vertices

    def heuristic(self):
        return 1

    def get_vertex(coordinates):
        for vertex in self.vertices:
            if vertex.coordinates == coordinates:
                return vertex
        return None

    def __str__(self):
        out = ''
        row = 0
        col = 0
        vertex = get_vertex((row, col))
        while vertex:
            out = out + str(vertex)
            col = col + 1
            vertex = get_vertex((row, col))
            if vertex is None:
                out = out + '\n'
                row = row + 1
                col = 0
                vertex = get_vertex((row, col))
        return out
