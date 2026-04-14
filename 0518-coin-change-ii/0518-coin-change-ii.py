class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        '''
        memo = {}
        def recursion(index,currentSum):
            nonlocal memo

            if index == 0:
                return currentSum % coins[0] == 0
            
            if (index,currentSum) in memo:
                return memo[(index,currentSum)]

            pick    = recursion(index, currentSum - coins[index])
            notPick = recursion(index-1, currentSum)

            ways = pick + notPick
            memo[(index,currentSum)] = ways

            return ways

        return recursion(len(coins)-1,amount)
        '''
        
        dp = []
        for i in range(len(coins)):
            tempArray = [0]*(amount+1)
            dp.append(tempArray)
        
        for i in range(len(coins)):
            dp[i][0] = 1

        for t in range(amount + 1):
            if t % coins[0] == 0:
                dp[0][t] = 1

        for i in range(1,len(dp)):
            for j in range(amount+1):
                pick = 0
                if coins[i] <= j:
                    pick    = dp[i][j - coins[i]]
                notPick = dp[i-1][j]
                dp[i][j] = pick + notPick
        return dp[-1][amount]
                





            
            

        