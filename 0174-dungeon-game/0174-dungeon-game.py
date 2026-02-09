class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        memo = {}
        
        def recursion(row,col):
            if row < 0 or col < 0 or row >= len(dungeon) or col >= len(dungeon[0]):
                return float("inf")

            if row == len(dungeon)-1 and col == len(dungeon[0])-1:
                return max(1, 1 - dungeon[row][col])

            if (row, col) in memo:
                return memo[(row, col)]

            right =  recursion(row,col+1)
            down  =  recursion(row+1,col)
            minHealthNeeded = min(right,down) 

            memo[(row, col)] = max(1, minHealthNeeded - dungeon[row][col])
            return memo[(row, col)]

        return recursion(0,0)