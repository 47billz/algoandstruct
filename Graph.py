'''
Symbol graph - No more than one edge between 2 nodes and No loops
Example Vertices: v1, v2, v3, ...
Example edge: (v1,v2) #An edge connecting v1 to v2

Internal structure: Adjacency list -> dict() + list
edges = {
            v1 : [v2, v3, v4],
            v2 : [v3]
            v3 : []
        }
Space complexity O(V + E)
'''

class Graph:
    ''' Undirected graph, uses dict() of lists internally'''
    def __init__(self):
        ''' Construct an empty Graph'''
        self.edges = {}
    
    def addVertex(self, v,):
        if v not in self.edges:
            self.edges[v] = [] 

    def addEdge(self,from_v,to_v):
        if from_v not in self.edges:
            self.edges[from_v] = []
        if to_v not in self.edges:
            self.edges[to_v] = []

        #Connected the vertices (Two conditions -> Undirected )
        if to_v not in self.edges[from_v]:
            self.edges[from_v].append(to_v)
        if from_v not in self.edges[to_v]:
            self.edges[to_v].append(from_v)
        
    def isEdge(self, from_v, to_v):
        ''' Check if an edge exists'''
        if to_v not in self.edges:
            return False
        if from_v not in self.edges:
            return False
        
        return to_v in self.edges[from_v]
    
    def loadGraph(self, edges):
        for v in edges:
            self.addVertex(v)
            for neighbor in edges[v]:
                self.addEdge(neighbor,v)