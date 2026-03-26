class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        visitedSet = set()
        hashMap = {}   

        def dfs(row, col, block):
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return 0
            if grid[row][col] != 1:
                return 0
            if (row, col) in visitedSet:
                return 0
            visitedSet.add((row, col))
            grid[row][col] = block
            length = 1
            length += dfs(row, col + 1, block)
            length += dfs(row + 1, col, block)
            length += dfs(row, col - 1, block)
            length += dfs(row - 1, col, block)
            return length

        block = 2

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    visitedSet.clear()
                    hashMap[block] = dfs(i, j, block)
                    block += 1

        maxAnswer = 0
        hasZero = False

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    hasZero = True
                    currentLength = 1
                    areaUsed = set()
                    
                    if j + 1 < len(grid[0]) and grid[i][j + 1] not in areaUsed:
                        if grid[i][j + 1] in hashMap:
                            currentLength += hashMap[grid[i][j + 1]]
                        areaUsed.add(grid[i][j + 1])

                    if i + 1 < len(grid) and grid[i + 1][j] not in areaUsed:
                        if grid[i + 1][j] in hashMap:
                            currentLength += hashMap[grid[i + 1][j]]
                        areaUsed.add(grid[i + 1][j])

                    if j - 1 >= 0 and grid[i][j - 1] not in areaUsed:
                        if grid[i][j - 1] in hashMap:
                            currentLength += hashMap[grid[i][j - 1]]
                        areaUsed.add(grid[i][j - 1])

                    if i - 1 >= 0 and grid[i - 1][j] not in areaUsed:
                        if grid[i - 1][j] in hashMap:
                            currentLength += hashMap[grid[i - 1][j]]
                        areaUsed.add(grid[i - 1][j])

                    maxAnswer = max(maxAnswer, currentLength)

        if hasZero == False:
            return len(grid) * len(grid[0])

        return maxAnswer