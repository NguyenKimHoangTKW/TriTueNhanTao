graph = {
    1: [3, 4, 8],
    2: [5 ,9, 10],
    3: [1, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 6, 9],
    6: [3, 5],
    7: [4, 8, 10],
    8: [1, 7],
    9: [2, 5],
    10: [2, 7]
}

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None

# Tìm đường đi từ Node-1 đến Node-10 và quay lại sử dụng các cây cầu khác nhau.
path_to_10 = find_path(graph, 1, 10)
if (5 in path_to_10) or (7 in path_to_10):
    bridge_used = {5} if (5 in path_to_10) else {7}
    remaining_bridge = {5, 7}.difference(bridge_used)
    
    if remaining_bridge:
        removed_bridge = remaining_bridge.pop()
        if removed_bridge in graph and bridge_used:
# Kiểm tra xem cây cầu có trong danh sách hay không trước khi gỡ bỏ
            if removed_bridge in graph[bridge_used.pop()]:
                graph[bridge_used.pop()].remove(removed_bridge)
    
    print("Đường đi từ Node -1 đến Node -10:", *path_to_10)
    print("Đường đi từ Node -10 quay lại Node -1:", *find_path(graph, 10, 1))
else:
    print("Đường đi từ Node -1 đến Node -10:", *path_to_10)
    print("Đường đi từ Node -10 quay lại Node -1:", *find_path(graph, 10, 1))
