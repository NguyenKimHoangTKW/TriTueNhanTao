graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['E', 'B'],
    'D': ['F'],
    'E': ['F'],
    'F': []
}

def dfs(graph, start, end, path=[]):
    path = path + [start]
    
    if start == end:
        return path
    
    if start not in graph:
        return None
    
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = dfs(graph, node, end, path)
            if newpath:
                if shortest is None or len(newpath) < len(shortest):
                    shortest = newpath
                    
    return shortest

print(dfs(graph, "A", "F"))
