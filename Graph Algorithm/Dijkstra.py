import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(n, edges, src):
    graph = {i: [] for i in range(n)}
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))  # If the graph is undirected, include this line

    min_heap = [(0, src)]
    distances = {i: float('inf') for i in range(n)}
    distances[src] = 0
    visited = set()

    while min_heap:
        curr_dist, u = heapq.heappop(min_heap)
        if u in visited:
            continue
        visited.add(u)

        for v, weight in graph[u]:
            if v not in visited:
                distance = curr_dist + weight
                if distance < distances[v]:
                    distances[v] = distance
                    heapq.heappush(min_heap, (distance, v))

    return distances

# Define the graph parameters
n = 5
edges = [[0, 1, 10], [0, 2, 3], [1, 3, 2], [2, 1, 4], [2, 3, 8], [2, 4, 2], [3, 4, 5]]
src = 0

# Run Dijkstra's algorithm
distances = dijkstra(n, edges, src)
print("Shortest distances from node 0:", distances)

# Graph Visualization
G = nx.Graph()
for u, v, w in edges:
    G.add_edge(u, v, weight=w)

pos = nx.spring_layout(G)
edge_labels = {(u, v): w for u, v, w in edges}

nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=15, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)
plt.show()
