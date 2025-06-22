import math
class Solution:
    def numSquares(self, n: int) -> int:
        if n == 1:
            return 1

        max_root = math.isqrt(n)
        numbers = [i*i for i in range(max_root, 0, -1)]
        print(numbers)

        leastNumberOfPerfectSquare = float('inf')
        memo = {}

        def recursion(currentNumber,coinCount):

            nonlocal leastNumberOfPerfectSquare, n, numbers, memo
            
            if coinCount >= leastNumberOfPerfectSquare:
                return

            if currentNumber in memo and coinCount >= memo[currentNumber]:
                return memo[currentNumber]
            memo[currentNumber] = coinCount
            
            if currentNumber == 0:
                leastNumberOfPerfectSquare = min(leastNumberOfPerfectSquare,coinCount)
                return

            for num in numbers:
                if num > currentNumber:
                    continue
                recursion(currentNumber-num,coinCount+1)



            return

        recursion(n,0)
        return leastNumberOfPerfectSquare
