class Solution:
    def fib(self, n: int) -> int:

        if n == 0:
            return 0 

        if n == 1:
            return 1 

        memo = {}

        def recursion(index):
            nonlocal memo

            if index == 0:
                return 0

            if index == 1:
                return 1
            
            if index in memo:
                return memo[index]
            
            oneStepLast = recursion(index-1)
            twoStepLast = recursion(index-2)

            memo[index] = oneStepLast + twoStepLast

            return memo[index]
            
        return recursion(n)


        