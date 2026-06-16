class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        n = str(n)
        ans = 0
        for i in range(len(n)):
            ans += int(n[i])

        return ans

        