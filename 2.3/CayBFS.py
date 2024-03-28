graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E','F'],
    'C': [],
    'D': ['G','H', 'I'],
    'E': [],
    'F': [],
    'G': [],
    'H': [],
    'I': ['J','K'],
    'J': [],
    'K': ['L', 'M', 'N'],
    'L': [],
    'M': [],
    'N': []
}

def dfs(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            new_path = dfs(graph, node, end, path)
            if new_path:
                return new_path

    return "Không tìm thấy đường đi từ A đến M"

path = dfs(graph, 'A', 'M')

print(f"Đường đi tối ưu từ A đến M là: {path}")
