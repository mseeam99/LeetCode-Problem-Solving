class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        dp = []
        for i in range(len(text1)+1):
            newArray = [0]*(len(text2)+1)
            dp.append(newArray)
        
        for i in range(1,len(text1)+1):

            for j in range(1,len(text2)+1):

                if (text1[i-1] == text2[j-1]):
                    val = (1 + dp[i-1][j-1])
                    dp[i][j] = val
                    

                else:
                    x = dp[i][j-1]
                    y = dp[i-1][j]
                    val = max(x,y)
                    dp[i][j] = val
                    


        
            

        return dp[len(text1)][len(text2)]
            


            
            


            



        