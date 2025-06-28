from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        def dfs(r,c):
            visited.add((r,c))
            dirn = [(1,0),(-1,0),(0,1),(0,-1)]
            for dr,dc in dirn:
                newr = r + dr
                newc = c + dc
                if (
                    newr in range(rows) and 
                    newc in range(cols) and 
                    (newr,newc) not in visited and
                    grid[newr][newc] != "0"
                ):
                    dfs(newr,newc)
            return 1
        
        result = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != "0" and (i,j) not in visited:
                    result += dfs(i,j)
        
        return result