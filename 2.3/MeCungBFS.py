maze = {
    'A': ['B', 'E'],
    'B': ['A', 'C'],
    'C': ['B', 'D', 'F'],
    'D': ['C', 'G'],
    'E': ['A', 'F'],
    'F': ['C', 'E', 'G', 'M'],
    'G': ['D', 'F', 'H'],
    'H': ['G', 'I', 'L'],
    'I': ['H', 'J'],
    'J': ['I', 'K', 'M'],
    'K': ['J', 'N'],
    'L': ['H', 'M'],
    'M': ['F', 'J', 'L', 'N']
}

def bfs(maze, start, end):
    queue = [[start]]
    visited = set()
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in visited:
            neighbors = maze[node]
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                if neighbor == end:
                    return new_path
            visited.add(node)
    return "Không tìm thấy đường đi từ A đến M"
path = bfs(maze, 'A', 'M')
print(f"Đường đi tối ưu từ A đến M là: {path}")
