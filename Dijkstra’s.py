import heapq

def dijkstra(n, edges, source):
    adj = {i: [] for i in range(n)}

    for s, d, weight in edges:
        adj[s].append((d, weight)) 

    shortest_path = {}
    minHeap = [[0, source]]  

    while minHeap:
        weight, node = heapq.heappop(minHeap)

        if node in shortest_path: 
            continue

        shortest_path[node] = weight

        for neighbour_weight, neighbour in adj[node]:
            if neighbour not in shortest_path:
                heapq.heappush(minHeap, [weight + neighbour_weight, neighbour])

    return shortest_path
