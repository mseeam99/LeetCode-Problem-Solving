class Solution:
    def tribonacci(self, n: int) -> int:

        memo = {}

        def recursion(index):
            nonlocal memo
            if index == 0:
                return 0
            if index == 1:
                return 1
            if index == 2:
                return 1
            
            if index in memo:
                return memo[index]

            memo[index] = recursion(index-1) + recursion(index-2) + recursion(index-3)

            return memo[index]
        
        return recursion(n)
            

        