#kruskals algorithm


class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

class UnionFind:
    def __init__(self,size):

        self.size = size
        self.numComponents = size

        self.sz = [1] * size #size of each component
        self.id = [i for i in range(size)]

    
    def find(self,p):

        root = p
        while root != self.id[root]:
            root = self.id[root]

        #path compression

        while p != root:
            next_node = self.id[p]
            self.id[p] = root
            p = next_node

        return root
    
    def connected(self, p, q):

        return self.find(p) == self.find(q)


    def componentSize(self,p):
        return self.sz[self.find(p)]
    

    def size(self):
        return self.size
    
    def components(self):
        return self.numComponents
    
    def union(self,p,q):

        if self.connected(p,q):
            return
        

        root1 = self.find(p)
        root2 = self.find(q)

        if self.sz[root1] < self.sz[root2]:
            self.sz[root2] += self.sz[root1]
            self.id[root1] = root2
            self.sz[root1] = 0
            
        else:
            self.sz[root1] += self.sz[root2]
            self.id[root2] = root1
            self.sz[root2] = 0

        self.numComponents -= 1


def kruskals(edges, num_vertices):

    edges.sort(key=lambda edge: edge.weight)

    uf = UnionFind(num_vertices)

    mst = []

    for edge in edges:
        if not uf.connected(edge.src,edge.dest):
            uf.union(edge.src,edge.dest)
            mst.append(edge)

    return mst


edges = [
    Edge(0, 1, 10),
    Edge(0, 2, 6),
    Edge(0, 3, 5),
    Edge(1, 3, 15),
    Edge(2, 3, 4)
]

num_vertices = 4  # Number of vertices
mst = kruskals(edges, num_vertices)

print("Edges in the Minimum Spanning Tree:")
for edge in mst:
    print(f"{edge.src} - {edge.dest}: {edge.weight}")