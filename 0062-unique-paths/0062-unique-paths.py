class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for i in range(m-2,-1,-1):
            currentRow = [1] * n
            for j in range(n-2,-1,-1):
                currentRow[j] = currentRow[j+1] + row[j]
            row = currentRow
        return row[0]