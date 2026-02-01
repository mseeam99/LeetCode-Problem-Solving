class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}

        def recursion(index):
            nonlocal memo

            if index > n:
                return 0
            
            if index == n:
                return 1
            
            if index in memo:
                return memo[index]

            oneStep = recursion(index+1)
            twoStep = recursion(index+2)

            memo[index] = oneStep + twoStep

            return oneStep + twoStep

        return recursion(0)
            

        