class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
    
        dp = []
        for i in range(len(str1)+1):
            tempArray = [0]*(len(str2)+1)
            dp.append(tempArray)
        
        for j in range(len(dp[0])):
            if j <= len(str2)-1 and str2[j] == str1[0]:
                dp[0][j] = 1
        
        for i in range(len(str1)+1):
            for j in range(len(str2)+1):        
                pick = float("-inf")
                if i-1 >= 0 and j-1 >= 0 and str1[i-1] == str2[j-1]:
                    pick = 1 + dp[i-1][j-1]
                notPick = max(dp[i-1][j],dp[i][j-1])
                dp[i][j] = max(pick,notPick)
        

        i = len(dp)-1
        j = len(dp[0])-1
        string = ""
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                string += str1[i-1]
                i-=1
                j-=1
            
            elif dp[i-1][j] > dp[i][j-1]:
                string += str1[i-1]
                i -= 1
            else:
                string += str2[j-1]
                j -= 1
        

        while i > 0:
            string += str1[i-1]
            i -= 1

        while j > 0:
            string += str2[j-1]
            j -= 1

            

        return string[::-1]





