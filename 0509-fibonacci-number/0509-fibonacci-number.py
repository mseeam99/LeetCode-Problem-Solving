class Solution:
    def fib(self, n: int) -> int:



       

        def recursion(index):
            if index == 0:
                return 0
            if index == 1:
                return 1

            return recursion(index-1) + recursion(index-2)

        return recursion(n)
        





        