class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        #memo
        memo = {}
        def recursion(index):
            nonlocal memo
            if index > n:
                return 0
            if index == n:
                return 1
            if index in memo:
                return memo[index]
            ways = recursion(index+1) + recursion(index+2)
            memo[index] = ways
            return ways
        return recursion(0)
        '''

        #tabulation
        if n == 0:
            return 0 
        elif n == 1:
            return 1
        if n == 2:
            return 2  
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

        
        