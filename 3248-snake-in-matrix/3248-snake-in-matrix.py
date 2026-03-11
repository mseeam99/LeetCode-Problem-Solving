class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:

        grid = []

        for i in range(n):
            array = []
            for j in range(n):
                val = (i * n) + j
                array.append(val)
            grid.append(array)
        
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
                
    
        

        