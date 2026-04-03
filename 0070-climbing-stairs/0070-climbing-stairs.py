class Solution:
    def climbStairs(self, n: int) -> int:

        memo = [0] * (n+1)

        def recursion(index):

            if index > n:
                return 0

            if index == n:
                return 1
            
            if memo[index] != 0:
                return memo[index]
       
            onestep = recursion(index+1)
            twostep = recursion(index+2)
            memo[index] = onestep + twostep
            return memo[index]

        
        return recursion(0)

        