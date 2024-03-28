from collections import deque

# Định nghĩa đồ thị bằng danh sách kề
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F", "G"],
    "D": ["B", "H", "I"],
    "E": ["B", "J", "K"],
    "F": ["C", 'L', 'M'],
    'G': ['C', 'N', 'O'],
    'H': ['D'],
    'I': ['D'],
    'J': ['E'],
    'K': ['E'],
    'L': ['F'],
    'M': ['F'],
    'N': ['G'],
    'O': ['G']
}

# Thuật toán BFS để tìm đường đi ngắn nhất
def bfs_shortest_path(graph, start, goal):
    
   # Tạo hàng đợi cho BFS và đưa đỉnh gốc vào hàng đợi
   queue = deque()
   queue.append((start, [start]))

   while queue:
       node, path = queue.popleft()

       if node == goal:
           return path

       for neighbor in graph.get(node, []):
           if neighbor not in path:
               new_path = list(path)
               new_path.append(neighbor)
               queue.append((neighbor, new_path))

# Tìm và in ra đường đi ngắn nhất từ A đến L
shortest_path = bfs_shortest_path(graph, start="A", goal="L")
print("Đường đi từ A đến L:", " -> ".join(shortest_path))
