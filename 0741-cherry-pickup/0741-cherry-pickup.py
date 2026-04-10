class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        memo = {}

        def dfs(r1, c1, r2):
            c2 = r1 + c1 - r2

            # out of bounds
            if r1 >= n or c1 >= n or r2 >= n or c2 >= n:
                return float("-inf")

            # thorn cell
            if grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return float("-inf")

            # reached destination
            if r1 == n - 1 and c1 == n - 1:
                return grid[r1][c1]

            if (r1, c1, r2) in memo:
                return memo[(r1, c1, r2)]

            cherries = grid[r1][c1]

            if r1 != r2 or c1 != c2:
                cherries += grid[r2][c2]

            bestNext = max(
                dfs(r1 + 1, c1, r2 + 1),  # down, down
                dfs(r1 + 1, c1, r2),      # down, right
                dfs(r1, c1 + 1, r2 + 1),  # right, down
                dfs(r1, c1 + 1, r2)       # right, right
            )

            memo[(r1, c1, r2)] = cherries + bestNext
            return memo[(r1, c1, r2)]

        ans = dfs(0, 0, 0)
        return max(0, ans)