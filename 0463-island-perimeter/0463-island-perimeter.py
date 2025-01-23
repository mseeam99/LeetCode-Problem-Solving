class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        def backTracking(r,c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
                return 1
            if (r,c) in visited:
                return 0
            visited.add((r,c))
            totalLand  = backTracking(r,c+1)
            totalLand += backTracking(r+1,c)
            totalLand += backTracking(r,c-1)
            totalLand += backTracking(r-1,c)
            return totalLand
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return backTracking(i,j)