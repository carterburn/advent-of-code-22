import sys
if len(sys.argv) > 1:
    fname = sys.argv[1]
else:
    fname = 'test.txt'
with open(fname,'r') as fi:
    lines = list(map(str.strip,fi.readlines()))

class Node:
    def __init__(self, elevation):
        self.elevation = elevation
        # all edges have implicit weight of 1
        self.edges = []

    def __str__(self):
        return 'Node<Elevation: ' + str(self.elevation) + ' (' + chr(self.elevation+ord('a')) + ')' + ' # Edge: ' + str(len(self.edges)) + '>'

def create_node(graph, charmap, row, col):
    if charmap[row][col] == 'S':
        elevation = ord('a') - ord('a')
    elif charmap[row][col] == 'E':
        elevation = ord('z') - ord('a')
    else:
        elevation = ord(charmap[row][col]) - ord('a')
    graph[(row,col)] = Node(elevation)
    
def add_edges(graph, charmap, row, col):
    # all nodes will have 4 edges, except if row or col == 0 or last row/col
    candidates = []
    cur = graph[(row,col)]
    if row != 0:
        candidates.append((row-1,col))
    if row != len(charmap)-1:
        candidates.append((row+1,col))
    if col != 0:
        candidates.append((row,col-1))
    if col != len(charmap[0])-1:
        candidates.append((row,col+1))

    # for each candidate node, determine if elevation is acceptable to add node
    for c in candidates:
        if graph[c].elevation <= cur.elevation+1:
            cur.edges.append(c)
    
# create a char-map of the input
inp = []
for line in lines:
    inp.append([c for c in line])

graph = {}
S = None
E = None
for row in range(len(inp)):
    for col in range(len(inp[row])):
        create_node(graph,inp,row,col)
        if inp[row][col] == 'S':
            S = (row,col)
        if inp[row][col] == 'E':
            E = (row,col)

for row,col in graph:
    add_edges(graph,inp,row,col)

def min_dist(Q, dist):
    # iterate through dist and return vertex with min dist
    min_dist = 10000000
    min_vert = None
    for v in Q:
        if dist[v] == None:
            continue
        if dist[v] < min_dist:
            min_dist = dist[v]
            min_vert = v
    return min_vert

# implement dijkstra's algorithm following wikipedia
# dist: map w/ current distance from source to all other nodes
dist = {}
# prev: pointers to previous-hop nodes on the shortest path from source to v
# implemented by indexing on coordinate and provides the previous-hop in the
# sequence from source -> coordinate
prev = {}
# Q is a set of vertices that should be implemented like a priority queue with
# the min dist (from dist array). as opposed to a priority queue, this will be a
# search each time using dist array
Q = []
for v in graph.keys():
    dist[v] = None # "infinity" value
    prev[v] = None # "undefined" value
    Q.append(v)
dist[S] = 0
prev[S] = None

# dijkstra time
while len(Q) != 0:
    u = min_dist(Q, dist)
    Q.remove(u)
    if u == E:
        break

    for v in graph[u].edges:
        if v not in Q:
            continue
        alt = dist[u] + 1 # all edges are size 1 with valid edges
        if dist[v] == None or alt < dist[v]:
            dist[v] = alt
            prev[v] = u

path = []
u = E
while prev[u] != None:
    path.append(u)
    u = prev[u]

print('answer:',len(path))
