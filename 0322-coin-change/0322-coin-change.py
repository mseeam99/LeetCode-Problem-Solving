class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        memo = {}

        def recursion(index,totalSum):

            if (index >= len(coins)) or (totalSum > amount):
                return float("+inf")
            
            if totalSum == amount:
                return 0
            
            if (index,totalSum) in memo:
                return memo[(index,totalSum)]

            pick = 1 + recursion(index,totalSum+coins[index])
            notPick = 0 + recursion(index+1,totalSum)

            bestDeal = min(pick,notPick)
            memo[(index,totalSum)] = bestDeal
            return bestDeal
        
        answer = recursion(0,0)
        return -1 if answer >= float(+inf) else answer

            


        