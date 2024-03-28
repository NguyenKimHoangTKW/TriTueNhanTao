def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next_node in graph[start] - visited:
        dfs(graph, next_node, visited)

# Đồ thị ví dụ
graph = {
    'A': {'B', 'S'},
    'B': {'A'},
    'C': {'D', 'E', 'F', 'S'},
    'D': {'C'},
    'E': {'C', 'H'},
    'F': {'C', 'G'},
    'G': {'F', 'S'},
    'H': {'E', 'G'},
    'S': {'A', 'C', 'G'}
}

# Tìm đường đi từ A đến B
dfs(graph, 'A')
