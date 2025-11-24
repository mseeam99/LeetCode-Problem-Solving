class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:

        grid = [[0]*n for _ in range(m)]
        for r, c in guards:
            grid[r][c] = "G"
        for r, c in walls:
            grid[r][c] = "W"

        mySet = set()

        for i in range(m):
            possible = False
            for j in range(n):
                if grid[i][j] == "G":
                    possible = True
                elif grid[i][j] == "W":
                    possible = False
                elif possible == True:
                    mySet.add((i,j))
        
        for i in range(m):
            possible = False
            for j in range(n-1,-1,-1):
                if grid[i][j] == "G":
                    possible = True
                elif grid[i][j] == "W":
                    possible = False
                elif possible == True:
                    mySet.add((i,j))
        
        for i in range(n):
            possible = False
            for j in range(m):
                if grid[j][i] == "G":
                    possible = True
                elif grid[j][i] == "W":
                    possible = False
                elif possible == True:
                    mySet.add((j,i))

        for i in range(n):
            possible = False
            for j in range(m-1,-1,-1):
                if grid[j][i] == "G":
                    possible = True
                elif grid[j][i] == "W":
                    possible = False
                elif possible == True:
                    mySet.add((j,i))

        for i in range(len(guards)):
            l,r = guards[i][0],guards[i][1]
            mySet.add((l,r))
        for i in range(len(walls)):
            l,r = walls[i][0],walls[i][1]
            mySet.add((l,r))
        return m * n - len(mySet)
                    
