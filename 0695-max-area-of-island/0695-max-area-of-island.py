class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        maximumArea = 0
        localArea = [0]
        visited = set()

        def backTrack(r,c,localArea):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == 0 or (r,c) in visited:
                return

            visited.add((r,c))

            backTrack(r,c+1,localArea)
            backTrack(r+1,c,localArea)
            backTrack(r,c-1,localArea)
            backTrack(r-1,c,localArea)

            localArea[0]+=1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i,j) not in visited and grid[i][j] == 1:
                    backTrack(i,j,localArea)
                    maximumArea = max(maximumArea,localArea[0])
                    localArea[0] = 0

        return maximumArea

        