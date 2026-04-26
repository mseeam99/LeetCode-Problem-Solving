class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        dp = []
        for i in range(len(s)+1):
            tempArray = [-1] * (len(t)+1)
            dp.append(tempArray)
         
        # s * t = m * n array


        def recursion(index1,index2):

            if index2 == 0:
                return 1

            if index1 == 0:
                return 0

            if dp[index1][index2] != -1:
                return dp[index1][index2]

            pick = 0
            notPick = 0

            if s[index1-1] == t[index2-1]:
                pick = recursion(index1-1,index2-1) + recursion(index1-1,index2)
            else:
                notPick = recursion(index1-1,index2)

            dp[index1][index2] = pick + notPick
            return dp[index1][index2]


        
        return recursion(len(s),len(t))



        