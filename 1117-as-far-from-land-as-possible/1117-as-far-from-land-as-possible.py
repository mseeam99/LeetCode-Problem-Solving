class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:

        visitedSet = set()
        myQueue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    myQueue.append([i,j])
                    visitedSet.add((i,j))

        print(myQueue)

        result = -1
        if not myQueue or len(visitedSet) == len(grid) * len(grid[0]):
            return -1

        while len(myQueue) != 0 :

            row,col = myQueue.popleft()

            result = grid[row][col]

            if min(row,col+1) >= 0 and max(row,col+1) < len(grid) and (row,col+1) not in visitedSet and grid[row][col+1]==0:
                myQueue.append([row,col+1])
                grid[row][col+1] = grid[row][col] + 1

            if min(row+1,col) >= 0 and max(row+1,col) < len(grid) and (row+1,col) not in visitedSet and grid[row+1][col]==0 :
                myQueue.append([row+1,col])
                grid[row+1][col] = grid[row][col] + 1

            if min(row,col-1) >= 0 and max(row,col-1) < len(grid) and (row,col-1) not in visitedSet and grid[row][col-1]==0:
                myQueue.append([row,col-1])
                grid[row][col-1] = grid[row][col] + 1

            if min(row-1,col) >= 0 and max(row-1,col) < len(grid) and (row-1,col) not in visitedSet and grid[row-1][col]==0:
                myQueue.append([row-1,col])
                grid[row-1][col] = grid[row][col] + 1

        if result == -1:
            return result
        else:
            return result-1
            







                

        