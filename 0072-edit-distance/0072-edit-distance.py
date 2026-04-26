class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        if (len(word1) == 0 and len(word2) > 0) or (len(word2) == 0 and len(word1) > 0):
            return len(max(word1,word2))

        if not word1 and not word2:
            return 0
        
        dp = []
        for i in range(len(word1)):
            tempArray = [0] * (len(word2))
            dp.append(tempArray)

        def recursion(idxOne,idxTwo):

            if idxOne < 0:
                return idxTwo + 1
            
            if idxTwo < 0:
                return idxOne + 1
            
            if dp[idxOne][idxTwo] != 0:
                return dp[idxOne][idxTwo]

            if word1[idxOne] == word2[idxTwo]:

                dp[idxOne][idxTwo] =   0 + recursion(idxOne-1,idxTwo-1)
                return dp[idxOne][idxTwo]

            insert = 1 + recursion(idxOne,idxTwo-1)
            delete = 1 + recursion(idxOne-1,idxTwo)
            rplace = 1 + recursion(idxOne-1,idxTwo-1)

            dp[idxOne][idxTwo] = min(insert,delete,rplace)

            return min(insert,delete,rplace)

        
        recursion(len(word1)-1,len(word2)-1)


        return dp[len(word1)-1][len(word2)-1]







            
        
















