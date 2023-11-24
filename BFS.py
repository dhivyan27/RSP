from collections import deque


def bfs(graph,start):

    queue = deque([start])
    visited = set()

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
        
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                queue.append(neighbour)



graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs(graph, 'A')