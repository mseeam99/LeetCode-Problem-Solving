class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        s = text1
        t = text2
        lengthS = len(s)
        lengthT = len(t)

        # DP initialization
        dp = [[0] * (lengthT + 1) for _ in range(lengthS + 1)]

        # Fill DP table
        for row in range(1, lengthS + 1):
            for col in range(1, lengthT + 1):
                if s[row - 1] == t[col - 1]:
                    dp[row][col] = 1 + dp[row - 1][col - 1]
                else:
                    dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

        # Backtrack
        i, j = lengthS, lengthT
        longestCommonSubsequence = ""
        while i > 0 and j > 0:
            if s[i - 1] == t[j - 1]:
                longestCommonSubsequence += s[i - 1]
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            elif dp[i - 1][j] < dp[i][j - 1]:
                j -= 1
            else:  # tie case
                i -= 1

        longestCommonSubsequence = longestCommonSubsequence[::-1]
        return len(longestCommonSubsequence)