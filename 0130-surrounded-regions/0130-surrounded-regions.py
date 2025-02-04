from typing import List
import copy

class Solution:
    def solve(self, board: List[List[str]]) -> None:

        visited = set()
        toChange = set()
        isEnclosed = True 

        def backTrack(r, c):
            nonlocal isEnclosed  

            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                isEnclosed = False
                return

            if board[r][c] == "X" or (r, c) in visited:
                return  
            
            visited.add((r, c))  
            toChange.add((r, c))  

            backTrack(r, c + 1)  # Right
            backTrack(r + 1, c)  # Down
            backTrack(r, c - 1)  # Left
            backTrack(r - 1, c)  # Up

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i, j) not in visited:
                    toChange.clear()  
                    isEnclosed = True  

                    backTrack(i, j) 

                    if isEnclosed:
                        for x, y in toChange:
                            board[x][y] = "X"  

        return board 
