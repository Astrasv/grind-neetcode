"""
QUESTION
A distributed system of servers is represented as a tree with tree_nodes, numbered from 1 to tree_nodes. Moving between directly connected servers takes 1 unit of time.
A process needs to:
Start at the start_node server.
Complete tasks at servers listed in an array task_nodes[] of size num_tasks by visiting servers in any order.
End at the end_node server.
Determine the minimum time required to complete all tasks and reach the end_node server.

Note:
Edges are bidirectional.
It is guaranteed that task_nodes[] contains distinct elements.
It is guaranteed that start_node is not equal to end_node and it is not present in task_nodes[].

Example
tree_nodes = 4
tree_from = [1, 2, 2]
tree_to = [3, 3, 4]
start_node = 1, end_node = 2
num_tasks = 1
task_nodes = [4]

One of the possible paths is: 1 -> 3 -> 2 -> 4 -> 2

Hence, the total time taken is 4.
"""

import heapq
def dijk(graph,start):
    dist = [float('inf')] * len(graph)
    dist[start] = 0
    q = [(0,start)]
    visited = set()
    
    while q:
        wei,node = heapq.heappop(q)
        
        for nei_w, nei in graph[node]:
            if nei not in visited:
                new_dist = dist[node]+nei_w
                if new_dist < dist[nei]:
                    dist[nei] = new_dist
                    heapq.heappush(q,(dist[nei],nei))
    return dist


def apsp(graph):
    result = []
    num_node = len(graph)
    for start in range(num_node):
        dist = dijk(graph,start)
        result.append(dist)
    return result

permsarr = []
visited_tasks = set()
def perms(task_nodes,temparr):
    if len(task_nodes) == len(temparr):
        permsarr.append(temparr[::])
        return
    
    for task in task_nodes:
        if task not in visited_tasks:
            visited_tasks.add(task)
            temparr.append(task)
            perms(task_nodes,temparr)
            visited_tasks.remove(task)
            temparr.pop()
    
    return permsarr

def tsp(task_nodes,start_node,end_node,graph):
    task_perms = perms(task_nodes,[])
    print(task_perms)
    dist_mat = apsp(graph)
    max_dist = 0
    for perm in task_perms:
        curr_dist = 0
        for j,node in enumerate(perm):
            if j == 0:
                curr_dist += dist_mat[start_node][node]
            else:
                curr_dist += dist_mat[node-1][node]
        
        curr_dist += dist_mat[node][end_node]
        max_dist = max(curr_dist,max_dist)
    
    return max_dist
    
graph = {
    0: [(1, 2)],
    1: [(1, 2), (1, 3)],
    2: [(1, 0), (1, 1)],
    3: [(1, 1)]
}



print(tsp([3],0,1,graph))
    

# graph = {
#     0: [(1, 3), (2, 2)],
#     1: [(0, 3), (2, 4)],
#     2: [(2, 0), (1, 4), (3, 5)],
#     3: [(1, 0), (0, 1), (2, 5)],
#     4: [(2, 1), (1, 2), (3, 5)],
#     5: [(3, 2), (2, 3), (3, 4)]
# }



# for x in apsp(graph):print(x) 