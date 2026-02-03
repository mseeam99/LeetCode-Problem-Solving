class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        memo = {}

        def recursion(index,currentSum):

            nonlocal memo

            if index >= len(coins):
                return 0
            
            if currentSum > amount:
                return 0
            
            if currentSum == amount:
                return 1

            if (index,currentSum) in memo:
                return memo[(index,currentSum)]

            pick    = recursion(index, currentSum + coins[index])
            notPick = recursion(index+1, currentSum + 0)
            ways = pick + notPick
            memo[(index,currentSum)] = ways
            return ways

        return recursion(0,0)


            
            

        