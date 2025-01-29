class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid1), len(grid1[0])
        coordinates = set()
        
        def backTrackFirstOne(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid1[r][c] == 0 or (r, c) in coordinates:
                return
            coordinates.add((r, c))
            backTrackFirstOne(r, c + 1)
            backTrackFirstOne(r + 1, c)
            backTrackFirstOne(r, c - 1)
            backTrackFirstOne(r - 1, c)

        for i in range(rows):
            for j in range(cols):
                if grid1[i][j] == 1:
                    backTrackFirstOne(i, j)

        def backTrackFirstTwo(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid2[r][c] == 0:
                return True  
            
            if (r, c) not in coordinates:
                return False  
            
            grid2[r][c] = 0  

            up = backTrackFirstTwo(r - 1, c)
            down = backTrackFirstTwo(r + 1, c)
            left = backTrackFirstTwo(r, c - 1)
            right = backTrackFirstTwo(r, c + 1)

            if up and down and left and right:
                return True

        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1:
                    if backTrackFirstTwo(i, j):
                        count += 1

        return count
