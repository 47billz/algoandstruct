'''
- No two dimentional array in Python, Use a dict() for internal implementation
- Each element is a disctionary of dictionaries , eg:
{
    1:{2:4}
}
vertex u = 1, vertex v = 2, edge u--v = 4
'''

class DirectedGraphAM:
    ''' Adjacency Matrix Representation of a Graph (Motivation: Dense Graph) .'''
    def __init__(self, size):
        self.vertices = {}
        self.size = size #Assume we have a size
    
    def addEdge(self, u, v, weight):
        ''' add an edge u - v if it does not exist.'''
        if not u in self.vertices:
            self.vertices[u] = {}
        self.vertices[u][v] = weight #connect the new vertice to u with an edge of a certain weight
    
    def neighbors(self, u):
        ''' generate neighbors for a vertices'''
        if u in self.vertices:
            for v in self.vertices[u]:
                yield (v,self.vertices[u][v])

    def __repr__(self):
        rep = 'graph:['
        for u in range(self.size):
            if u in self.vertices:
                rep += str(u) + ':'
                for v in self.vertices[u]:
                    rep += '(' + str(v) + ',' + str(self.vertices[u][v]) + ')' + ','
        return rep + ']'