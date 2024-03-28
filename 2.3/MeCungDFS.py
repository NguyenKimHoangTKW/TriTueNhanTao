graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['H', 'I'],
    'E': [],
    'F': [],
    'G': [],
    'H': [],
    'I': ['J', 'K'],
    'J': [],
    'K': ['L', 'M']
}

def dfs(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = dfs(graph, node, end, path)
            if newpath: return newpath
    return None

print(dfs(graph, 'A', 'M'))