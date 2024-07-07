import heapq
import networkx as nx
import matplotlib.pyplot as plt

def bellman_ford(n, edges, src):
    distances = [float('inf')] * n
    distances[src] = 0

    # Relax all edges |V| - 1 times.
    for _ in range(n - 1):
        for u, v, w in edges:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w

    # Check for negative-weight cycles.
    for u, v, w in edges:
        if distances[u] != float('inf') and distances[u] + w < distances[v]:
            print("Graph contains a negative-weight cycle")
            return None

    return distances

# Define the graph parameters
n = 5
edges = [[0, 1, 10], [0, 2, 3], [1, 3, 2], [2, 1, 4], [2, 3, 8], [2, 4, 2], [3, 4, 5]]
src = 0

# Run Bellman-Ford algorithm
distances = bellman_ford(n, edges, src)
print("Shortest distances from node 0:", distances)

# Graph Visualization
G = nx.DiGraph()
for u, v, w in edges:
    G.add_edge(u, v, weight=w)

pos = nx.spring_layout(G)
edge_labels = {(u, v): w for u, v, w in edges}

nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=15, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)
plt.show()
