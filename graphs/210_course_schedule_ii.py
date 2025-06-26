from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prereq: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u,v in prereq:graph[v].append(u)
        
        indegree = [0] * numCourses
        for vertex in graph:
            for nei in graph[vertex]:
                indegree[nei] += 1
        
        queue = deque([])
        for node,deg in enumerate(indegree):
            if deg == 0:
                queue.append(node)
        
        topo = []

        while queue:
            popped = queue.popleft()
            topo.append(popped)
            for nei in graph[popped]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        
        if len(topo) == numCourses:
            return topo
        else:
            return []



