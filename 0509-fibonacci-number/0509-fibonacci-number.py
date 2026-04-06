class Solution:
    def fib(self, n: int) -> int:
        # memo

        
        memo = {}
        def recursion(index):
            if index in memo:
                return memo[index]
            if index == 0:
                return 0
            if index == 1:
                return 1
            memo[index] = recursion(index-1) + recursion(index-2)
            return memo[index]
        return recursion(n)
       

        #tabulation
        if n == 0:
            return 0
        if n == 1:
            return 1
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]


        








        