class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        grid = [[0 for _ in range(n)] for _ in range(n)]
        
        top = 0
        bottom = len(grid)-1
        left = 0
        right = len(grid[0])-1
        number = 1

        while top <= bottom and left <= right:

            for i in range(left,right+1):
                grid[top][i] = number
                number+=1
            top+=1

            for i in range(top,bottom+1):
                grid[i][right] = number
                number+=1
            right-=1

            for i in range(right,left-1,-1):
                grid[bottom][i] = number
                number+=1
            bottom -= 1

            for i in range(bottom,top-1,-1):
                grid[i][left] = number
                number+=1
            left += 1 

        return grid
            

