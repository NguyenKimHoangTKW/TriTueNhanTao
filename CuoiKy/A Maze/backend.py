import adjancy_matrix_gen
import copy


def backened(src, obstacles, destination):
    def min_distance(dist, sp_set): 
        min = 10**10
        global min_index
        for v in range(400):                       
            if sp_set[v] == False and dist[v]<=min:
                min = dist[v]
                min_index = v
        return min_index

    graph, size = copy.deepcopy(adjancy_matrix_gen.return_matrix())    
    parent = [-2 for i in range(400)]                   

    for value in obstacles:                        
        for z in range(size):                         
            graph[z][value] = 0

    dist = [10**10 for i in range(size)]                
    sp_set = [False for i in range(size)]            
    dist[src] = 0
    parent[src] = -1

    for i in range(size-1):
        u = min_distance(dist, sp_set)                  
        sp_set[u] = True
                                        
        for v in range(size):
            if sp_set[v] is False and graph[u][v] != 0 and dist[u] != 10**10 and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]
                parent[v] = u
    def ancestor(dest):
        list1 = []
        stop = dest
        while parent[stop] != -1:              
            list1.append(parent[stop])
            stop = parent[stop]

        return list1

    destination_parent = ancestor(destination)
    return destination_parent
