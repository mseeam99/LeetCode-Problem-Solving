class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:

        s = nums1
        t = nums2

        lengthS = len(s)
        lengthT = len(t)

        dp = []
        for i in range(lengthS + 1):
            dp.append([0] * (lengthT + 1))

        for row in range(1, lengthS + 1):
            for col in range(1, lengthT + 1):
                if s[row - 1] == t[col - 1]:
                    dp[row][col] = 1 + dp[row - 1][col - 1]
                else:
                    dp[row][col] = 0

        maxLength = 0
        for i in range(len(dp)):
            for j in range(len(dp[i])):
                maxLength = max(maxLength,dp[i][j])
        return maxLength
