class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        lastRow = [1] * n
        for i in range(m-2,-1,-1):
            newRow = [1] * n
            for j in range(n-2,-1,-1):
                newRow[j] = newRow[j+1] + lastRow[j]
            lastRow = newRow
        return lastRow[0]
        