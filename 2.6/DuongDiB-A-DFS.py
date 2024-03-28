graph = {
    'A': ['D', 'C'],
    'B': ['D'],
    'C': ['A', 'D'],
    'D': ['A', 'B', 'C']
}

visited = set()

def dfs(visited, graph, node, destination):
    if node not in visited:
        print(node)
        visited.add(node)
        if node == destination:
            return
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour, destination)

# Gọi hàm với điểm bắt đầu là B và điểm kết thúc là A
dfs(visited, graph, 'B', 'A')
