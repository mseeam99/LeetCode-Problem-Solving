class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:

        grid = []
        start = 0

        for i in range(n):
            array = []
            for j in range(start,start+n):
                array.append(j)
                start += 1
            grid.append(array)

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j] = (i * n) + j
        
        answer = 0
        i,j = 0,0

        for idx in range(len(commands)):
            if commands[idx] == "RIGHT":
                j += 1
            elif commands[idx] == "DOWN":
                i += 1
            elif commands[idx] == "LEFT":
                j -= 1
            elif commands[idx] == "UP":
                i -= 1
    
        return grid[i][j]                
                
    
        

        