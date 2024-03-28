from collections import deque

# Biểu diễn đồ thị dưới dạng danh sách kề
graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "E"],
    "D": ["B", "F"],
    "E": ["B", "C", "F"],
    "F": []
}

def bfs_shortest_path(graph, start, goal):
    visited = set()
    queue = deque([[start]])
    
    if start == goal:
        return [start]
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        if node not in visited:
            neighbours = graph[node]
            
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                
                if neighbour == goal:
                    return new_path
            
            visited.add(node)

# Kiểm tra hàm với trường hợp của bạn
duong_di_ngan_nhat = bfs_shortest_path(graph, 'A', 'F')
print("Đường đi ngắn nhất:", duong_di_ngan_nhat)
