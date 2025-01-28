class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        EMPTY, FRESH, ROTTEN = 0, 1, 2
        ROWS = len(grid)
        COLS = len(grid[0])

        fresh_oragne = 0
        time = -1

        queue = deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == EMPTY:
                    pass
                elif grid[i][j] == FRESH:
                    fresh_oragne += 1
                elif grid[i][j] == ROTTEN:
                    queue.append((i,j))

        if fresh_oragne == 0:
            return 0

        while queue:
            lengthOfQueue = len(queue)
            time+=1
            for _ in range(lengthOfQueue):
                i,j = queue.popleft()
                for r,c in [(i+1,j), (i-1,j), (i,j-1), (i,j+1)]:
                    if r >= 0 and r < ROWS and c >= 0 and c < COLS and grid[r][c] == FRESH:
                        grid[r][c] = ROTTEN
                        fresh_oragne-=1
                        queue.append((r,c))

        if fresh_oragne == 0:
            return time
        else:
            return -1        