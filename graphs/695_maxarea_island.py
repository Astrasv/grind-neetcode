from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def dfs(r, c):
            visited.add((r, c))
            area = 1
            dirn = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for dr, dc in dirn:
                newr, newc = r + dr, c + dc
                if (
                    newr in range(rows) and
                    newc in range(cols) and
                    (newr, newc) not in visited and
                    grid[newr][newc] == 1
                ):
                    area += dfs(newr, newc)
            return area

        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i, j) not in visited:
                    max_area = max(max_area, dfs(i, j))

        return max_area
