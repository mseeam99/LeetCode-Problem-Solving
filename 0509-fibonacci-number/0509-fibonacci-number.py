class Solution:
    def fib(self, n: int) -> int:
        # memo
        '''
        def recursion(index):
            if index == 0:
                return 0
            if index == 1:
                return 1
            return recursion(index-1) + recursion(index-2)
        return recursion(n)
        '''

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


        








        