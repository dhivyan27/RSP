class Graph:
    def __init__(self,Nodes):
        self.nodes = Nodes
        self.adj_list = {}

        for node in self.nodes:
            self.adj_list[node] = []

    def print_adj_lst(self):
        for node in self.nodes:
            print(node , " : " , self.adj_list[node])

    def add_edge(self,u,v):
        self.adj_list[u].append[v]
        self.adj_list[v].append[u]

    def find_degree(self,node):
        count = 0
        for _ in range(self.adj_list[node]):
            count +=1
        return count

    def remove_edge(self,u,v):
        self.adj_list[u].remove(v)
        self.adj_list[v].remove(u)