class Solution:
    def numWays(self, n: int, k: int) -> int:

        memo = {}

        def recursion(index):

            if index == 1:
                return k
            if index == 2:
                return k*k

            if index in memo:
                return memo[index]

            memo[index] = (k-1) * (recursion(index-1)+recursion(index-2))

            return memo[index]

        
        return recursion(n)






     