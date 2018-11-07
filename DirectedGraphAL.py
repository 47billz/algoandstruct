
'''
Design:
    Vertices labeled from 0 to (size- 1)
    A vector (list) of vertices
    Each element in list points to an adjecent list of it's neighbors and  wieghts between them.
    
'''

class DirectedGraphAL:
    '''Adjacency List Representation of Directed, weighted Graph (Motivation: Sparse Graphs)'''
    def __init__(self, size):
        self.size = size
        self.vertices = [None]*size #Assume we have a size and create empty slots with the size

    def addEdge(self, u, v, weight):
        ''' 
            Add node in list of vertice if not present
            Add an edge if not present,find & replace it if present [2 steps]
        '''
        if self.vertices[u] == None:
            self.vertices[u] = []

        for e in self.vertices[u]:
            if e[0] == v:
                self.vertices[u].remove(e)

        self.vertices[u].append( (v,weight) )
        
    def neighbors(self, u):
        '''wallk adjecency list and generate edges'''
        if self.vertices[u]:
            for e in self.vertices[u]:
                yield e
    
    def __repr__(self):
        rep = 'graph:['
        for u in range(self.size):
            if self.vertices[u]:
                rep += str(u) + ':'
                rep += ','.join(map(str,self.vertices[u]))
                rep += ';'
        return rep + ']'