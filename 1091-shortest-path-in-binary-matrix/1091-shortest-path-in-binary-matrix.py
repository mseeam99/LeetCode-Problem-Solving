class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        coordinated = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
        visited = set((0,0))
        queue = deque([(0,0,1)])
        while queue:
            row,col,length = queue.popleft()
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 1:
                continue
            if row == len(grid)-1 and col == len(grid[0])-1:
                return length
            for dr,dc in coordinated:
                if (row+dr, col+dc) not in visited:
                    queue.append((row+dr, col+dc, length+1))
                    visited.add((row+dr, col+dc))
        return -1

            



            


        