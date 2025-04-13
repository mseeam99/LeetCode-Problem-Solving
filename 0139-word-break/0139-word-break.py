class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [False] * (len(s)+1)
        dp[0] = True

        print(dp)

        print()
        print()
        print()

        print(wordDict)


        for i in range(len(s)):
            for word in wordDict:
                if dp[i] == True and s[i:i+len(word)] == word:
                    print("INDEX WE ARE PUTTING IN DP: ", (i+len(word)))
                    dp[i+len(word)] = True
                    print(dp)
                   

        return dp[-1]