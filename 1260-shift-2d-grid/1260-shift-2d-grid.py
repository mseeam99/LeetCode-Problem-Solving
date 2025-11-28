class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        elementTrack = grid[0][0]
        nextElementTrack = grid[0][0]

        def shiftValues():
            lastVal = grid[len(grid)-1][len(grid[0])-1]
            nonlocal elementTrack, nextElementTrack
            for row in range(len(grid)):
                for col in range(len(grid[row])):

                    if row == len(grid)-1 and col == len(grid[0])-1:
                        grid[0][0] = lastVal


                    if row == len(grid)-1 and col == len(grid[0])-1:
                        break
                    if col == len(grid[0])-1:    
                        if row+1 <= len(grid)-1:
                            nextElementTrack = grid[row+1][0]
                            grid[row+1][0] = elementTrack
                            elementTrack = nextElementTrack
                    else:
                        nextElementTrack = grid[row][col+1]
                        grid[row][col+1] = elementTrack
                        elementTrack = nextElementTrack
                
                    

           



        for i in range(k):
            shiftValues()
        return grid



        