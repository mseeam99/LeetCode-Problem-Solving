class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        dp = []
        for i in range(len(word1)+1):
            tempArray = [0]*(len(word2)+1)
            dp.append(tempArray)


        for i in range(1,len(word1)+1):


            for j in range(1,len(word2)+1):


                pick = float("-inf")
                if i-1 >= 0 and j-1 >= 0 and word1[i-1] == word2[j-1]:
                    pick    = 1 + dp[i-1][j-1]

                notPick = 0 + max(dp[i-1][j],dp[i][j-1])

                dp[i][j] = max(pick,notPick)


        print(dp)

        removalCount  = len(word1) - dp[len(word1)][len(word2)]
        additionCount = len(word2) - dp[len(word1)][len(word2)]

        totalChanges = abs(removalCount + additionCount)

        return totalChanges

                


        