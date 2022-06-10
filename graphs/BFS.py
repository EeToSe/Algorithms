def BFS(s,Adj):
    """ Breadth First Search
    Args:
        - s   staring vertex
        - Adj Adjacency list      
    """
    level = {}                      # level info of vertex v
    level[s] = 0 
    frontier = [s]                  # previous level
    parent = {}                     # parent of vertex v
    parent[s] = None                

    i = 0                           # start from level 0
    while frontier:
        i += 1                      # move to next level
        next = []                  
        for u in frontier:
            for v in Adj[u]:
                if v not in level:  # not seen in previous levels
                    level[v] = i
                    parent[v] = u
                    next.append(v)
        frontier = next

    return level, parent

if __name__ == "__main__":
    # init Adjacency list
    Adj = {}
    Adj['s'] = ['a', 'x']
    Adj['a'] = ['z']
    Adj['x'] = ['d','c']
    Adj['z'] = ['a']
    Adj['c'] = ['f','v']
    Adj['d'] = ['f']
    Adj['f'] = ['v']
    Adj['v'] = ['f']

    level, parent = BFS('s', Adj)
    print(parent)


