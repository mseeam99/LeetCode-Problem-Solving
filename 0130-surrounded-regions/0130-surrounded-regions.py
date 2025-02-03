from typing import List
import copy

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        copyOfBoard = copy.deepcopy(board)  # Properly copy the board

        visited = set()
        toChange = set()
        isEnclosed = True  # Flag to track if the region is enclosed

        def backTrack(r, c):
            nonlocal isEnclosed  # Use a flag to determine if it's enclosed

            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                isEnclosed = False  # If it touches the border, it's not enclosed
                return
            
            if board[r][c] == "X" or (r, c) in visited:
                return  # Stop recursion if we hit a wall or revisit
            
            visited.add((r, c))  # Mark cell as visited
            toChange.add((r, c))  # Track for conversion later

            # Explore in all 4 directions
            backTrack(r, c + 1)
            backTrack(r + 1, c)
            backTrack(r, c - 1)
            backTrack(r - 1, c)

        # Iterate over the board to find "O" regions
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i, j) not in visited:
                    toChange.clear()  # Reset tracking for each new region
                    isEnclosed = True  # Assume it's enclosed initially

                    backTrack(i, j)  # Start backtracking

                    if isEnclosed:
                        for x, y in toChange:
                            board[x][y] = "X"  # Only modify enclosed regions

        return board  # (Not necessary as function modifies in place)
