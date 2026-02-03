class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}

        def recursion(index,currentSum):
            nonlocal memo
            if index >= len(coins) or currentSum > amount:
                return float("inf")
            
            if currentSum == amount:
                return 0
            
            if (index,currentSum) in memo:
                return memo[(index,currentSum)]

            pick = 1 + recursion(index,currentSum+coins[index]) 
            notPick = 0 + recursion(index+1,currentSum+0)

            minCoins = min(pick,notPick)
            memo[(index,currentSum)] = minCoins
            return minCoins

        ans = recursion(0,0)
        if ans == float("inf"):
            return -1
        else:
            return ans
