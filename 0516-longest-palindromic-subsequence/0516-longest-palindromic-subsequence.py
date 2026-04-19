class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        def lcs(stringOne, stringTwo):

            dp = []
            for i in range(len(stringOne) + 1):
                row = [0] * (len(stringTwo) + 1)
                dp.append(row)

            for i in range(1, len(stringOne) + 1):
                for j in range(1, len(stringTwo) + 1):
                    if stringOne[i - 1] == stringTwo[j - 1]:
                        dp[i][j] = 1 + dp[i - 1][j - 1]
                    else:
                        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

            return dp[len(stringOne)][len(stringTwo)]

        return lcs(s, s[::-1])