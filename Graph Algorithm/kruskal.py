import networkx as nx
import matplotlib.pyplot as plt

# Tạo một đồ thị
G = nx.Graph()

# Thêm các cạnh với trọng số
edges = [
    ('1', '2', 5), 
    ('1', '3', 8), 
    ('1', '4', 10), 
    ('2', '4', 3), 
    ('2', '5', 7), 
    ('3', '4', 2), 
    ('3', '6', 9), 
    ('3', '7', 1), 
    ('4', '7', 11), 
    ('4', '5', 6), 
    ('5', '7', 12),
    ('5', '6', 14),
    ('6', '7', 4),
    ('2', '7', 13)
]

# Thêm các cạnh vào đồ thị
for edge in edges:
    G.add_edge(edge[0], edge[1], weight=edge[2])

# Thiết lập vị trí của các đỉnh
pos = nx.spring_layout(G)

# Vẽ đồ thị
plt.figure(figsize=(10, 7))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=15, font_weight='bold', edge_color='gray')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=12, font_weight='bold')
plt.title("Đồ thị có 7 đỉnh và 14 cạnh với trọng số dương")
plt.show()
