class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:

        memo = {}
       
        def recursion(r1,c1,r2):

            if (r1,c1,r2) in memo:
                return memo[(r1,c1,r2)]


            c2 = (r1+c1) - r2

            if r1 >= len(grid) or c1 >= len(grid) or r2 >= len(grid) or c2 >= len(grid):
                return (float("-inf"))
            
            if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return (float("-inf"))

            if (r1 == len(grid)-1 and c1 == len(grid)-1) or (r2 == len(grid)-1 and c2 == len(grid)-1):
                return grid[len(grid)-1][len(grid)-1]

            gain = grid[r1][c1]
            if (r1, c1) != (r2, c2):
                gain += grid[r2][c2]



            best = max(
                recursion(r1+1,c1,r2+1), # down, down
                recursion(r1+1,c1,r2),   # down, right
                recursion(r1,c1+1,r2+1), # right, down
                recursion(r1,c1+1,r2),   # right, right
            )

            memo[(r1,c1,r2)] = gain + best



            return gain + best

            




        answer = recursion(0,0,0)
        return max(0,answer)



        



        