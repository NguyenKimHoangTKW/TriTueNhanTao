graph = {
    'A': {'B': 10, 'C': 2},
    'B': {'A': 10, 'D': 3, 'E': 3},
    'C': {'A': 2, 'E': 3},
    'D': {'B': 3, 'F': 6},
    'E': {'B': 3, 'C': 3, 'F': 12},
    'F': {'D': 6, 'E': 12}
}

def dfs(graph, start, end, path=None):
    if path is None:
        path = [start]
    if start == end:
        return path
    shortest_path = None
    for neighbor in graph[start]:
        if neighbor not in path:
            new_path = dfs(graph, neighbor, end, path + [neighbor])
            if new_path:
                if shortest_path is None or len(new_path) < len(shortest_path):
                    shortest_path = new_path
    return shortest_path

# Tìm đường đi ngắn nhất từ A đến F
shortest_path = dfs(graph, 'A', 'F')

if shortest_path:
    print("Đường đi ngắn nhất:", shortest_path)
    print("Chiều dài của đường đi:", sum(graph[shortest_path[i]][shortest_path[i + 1]] for i in range(len(shortest_path) - 1)))
else:
    print("Không tìm thấy đường đi từ A đến F.")
