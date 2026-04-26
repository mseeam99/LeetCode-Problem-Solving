class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        dp = []
        for i in range(len(word1) + 1):
            tempArray = [-1] * (len(word2) + 1)
            dp.append(tempArray)

        def recursion(idxOne,idxTwo):

            if idxOne == 0:
                dp[idxOne][idxTwo] = idxTwo
                return idxTwo

            if idxTwo == 0:
                dp[idxOne][idxTwo] = idxOne
                return idxOne

            if dp[idxOne][idxTwo] != -1:
                return dp[idxOne][idxTwo]

            if word1[idxOne-1] == word2[idxTwo-1]:
                dp[idxOne][idxTwo] = recursion(idxOne-1,idxTwo-1)
            else:
                insert = 1 + recursion(idxOne,idxTwo-1)
                delete = 1 + recursion(idxOne-1,idxTwo)
                rplace = 1 + recursion(idxOne-1,idxTwo-1)
                dp[idxOne][idxTwo] = min(insert,delete,rplace)

            return dp[idxOne][idxTwo]

        recursion(len(word1), len(word2))

        return dp[-1][-1]

       