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

            ways = recursion(index+1) + recursion(index+2)
            memo[index] = ways
            return ways
            
            




        return recursion(0)


        
        