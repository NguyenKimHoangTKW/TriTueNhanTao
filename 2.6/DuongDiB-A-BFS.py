graph = {'B': ['D'], 'D': ['B', 'C', 'A'], 'A': ['D', 'C'], 'C': ['A', 'D']}

def bfs(graph, start, end):
    visited = []
    queue = [[start]]
    
    if start == end:
        return f"Điểm đầu là điểm cuối: {start}"
    
    while queue:
        path = queue.pop(0)
        node = path[-1]
        
        if node not in visited:
            neighbours = graph[node]
            
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                
                if neighbour == end:
                    return f"Đường đi từ {start} đến {end}: {' -> '.join(new_path)}"
            
            visited.append(node)

print(bfs(graph, 'B', 'A'))
