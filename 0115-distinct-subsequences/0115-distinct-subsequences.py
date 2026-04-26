class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # s * t = m * n array
        '''
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
        '''
            
        prev = [0] * (len(t) + 1)
        prev[0] = 1
        for i in range(1,len(s)+1):
            curr = [0]*(len(t)+1)
            curr[0] = 1
            for j in range(1,len(t)+1):
                pick, notPick = 0,0
                if s[i-1] == t[j-1]:
                    pick = prev[j-1] + prev[j]
                else:
                    notPick = prev[j]
                curr[j] = pick + notPick
            prev = curr
        return prev[-1]







        