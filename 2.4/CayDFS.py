graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    # Thêm các dòng sau để tạo kết nối hai chiều
    # và bao gồm các đỉnh cuối
    "H": [], "I": [], "J": [], "K": [],
    "L": [], "M": [], "N": [], "O": []
}

def dfs(graph, start, goal):
    stack = [(start, [start])]
    
    while stack:
        (node, path) = stack.pop()
        
        for next in set(graph[node]) - set(path):
            if next == goal:
                return path + [next]
            else:
                stack.append((next, path + [next]))

# Kiểm tra hàm với đồ thị và các đỉnh tương ứng
path = dfs(graph, "A", "L")
print("Đường đi từ A đến L:", path)
