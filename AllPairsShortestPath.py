import sys

graph = {
    0:{1:2,4:2},
    1:{2:3},
    2:{3:5, 4:1 },
    3:{0:8},
    4:{3:3}
}

def allPairsShortestPath(g):
    ''' Return distance structure as computed '''
    dist = {}
    pred = {}
    for u in g:
        pred[u] = {}                    #initialize predecessor for each vertex  
        dist[u] = {}                    #Initialize the dist matrix with empty columns
        for v in g:
            dist[u][v] = sys.maxsize    #initalize each cell with an infinite distance
            pred[u][v] = None
        
        dist[u][u] = 0                  #Zero distance from a vertex to itself
        pred[u][u] = None               #There is no distance from u to u
        for v in g[u]:
            dist[u][v] = g[u][v]        #start filling up the distance matrix (replace infinite distance with edge distance)
            pred[u][v] = u              #Fill up the predecesor matrix with direct edges
        
    for mid in g:
        for u in g:
            for v in g:
                newlen = dist[u][mid] + dist[mid][v]
                if newlen < dist[u][v]:
                    dist[u][v] = newlen
                    pred[u][v] = pred[mid][v]
    
    return (dist , pred)

def costructShortestPath(s, t, pred):
    ''' Reconstruct shortest path from s to t using infor from pred table '''
    path = [t]             #start at the destination
    while t != s:
        t = pred[s][t]     #move by predicessor(s,t) 
        if t is None:
            return None
        path.insert(0, t)  #insert path in the beginning of path
    
    return path