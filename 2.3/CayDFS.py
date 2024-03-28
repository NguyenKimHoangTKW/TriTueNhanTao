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
            newpath = dfs(graph, node, end, path)
            if newpath:
                return newpath
    return None

print(dfs(graph, 'A', 'M'))
