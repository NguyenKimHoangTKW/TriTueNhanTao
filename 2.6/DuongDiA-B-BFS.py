from collections import deque

# Đồ thị được biểu diễn dưới dạng danh sách kề
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

def bfs(graph, start, end):
    visited = set()
    queue = deque([[start]])
    
    if start == end:
        print(f"Điểm xuất phát và điểm đích giống nhau: {start}")
        return
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node not in visited:
            neighbours = graph[node]
            
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                
                if neighbour == end:
                    print("Tìm thấy đường đi:", *new_path)
                    return
            
            visited.add(node)

bfs(graph, 'A', 'B')
