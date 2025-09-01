class Solution:
    def arrangeCoins(self, n: int) -> int:
        totalUsed = 0
        for i in range(1,n+1):
            totalUsed += i
            if n - totalUsed < i+1:
                return i