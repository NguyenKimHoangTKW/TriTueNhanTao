from queue import Queue

# Đồ thị được biểu diễn dưới dạng danh sách kề
graph = {
    'A': {'B': 10, 'C': 2},
    'B': {'A': 10, 'D': 3, 'E': 3},
    'C': {'A': 2, 'D': 3, 'E': 3},
    'D': {'B': 3, 'C': 3, 'F': 12},
    'E': {'B': 3, 'C': 3, 'F': 4},
    'F': {'D': 12, 'E': 4}
}

def bfs_shortest_path(graph, start, goal):
    explored = set()
    queue = Queue()
    
    if start == goal:
        return f"Điểm xuất phát và điểm đích giống nhau: {start}"
    
    queue.put([start])
    
    while not queue.empty():
        path = queue.get()
        node = path[-1]
        
        if node not in explored:
            neighbors = graph[node]
            
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.put(new_path)
                
                if neighbor == goal:
                    return new_path
            
            explored.add(node)

shortest_path = bfs_shortest_path(graph, 'A', 'F')

if shortest_path:
    print("Đường đi ngắn nhất:", shortest_path)
    print("Chiều dài của đường đi:", sum(graph[shortest_path[i]][shortest_path[i + 1]] for i in range(len(shortest_path) - 1)))
else:
    print("Không tìm thấy đường đi từ A đến F.")
