class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        memo = {}
        def recursion(index,currentSum):
            nonlocal memo
            if index == 0:
                if currentSum % coins[0] == 0 :
                    return currentSum // coins[0]
                else:
                    return float("inf")
            pick = float("inf")
            if coins[index] <= currentSum:
                pick = 1 + recursion(index,currentSum-coins[index]) 
            notPick = 0 + recursion(index-1,currentSum)
            minCoins = min(pick,notPick)
            memo[(index,currentSum)] = minCoins
            return minCoins
        ans = recursion(len(coins)-1,amount)
        if ans == float("inf"):
            return -1
        else:
            return ans
        '''
        '''
        dp = []
        for i in range(len(coins)):
            tempArray = []
            if i == 0:
                tempArray = [1]*(amount+1)
            else:
                tempArray = [0]*(amount+1)
                tempArray[0] = 1
            dp.append(tempArray)
        
        for t in range(0,len(dp[0])):
            if t % coins[0] == 0:
                dp[0][t] = t // coins[0]
            else:
                dp[0][t] = float("inf")

        for i in range(1,len(coins)):
            for j in range(amount+1):
                pick = float("inf")
                if coins[i] <= j:
                    pick = 1 + dp[i][j-coins[i]]
                notPick = 0 + dp[i-1][j]
                dp[i][j] = min(pick,notPick)
            
        ans = dp[-1][-1]        
        if ans == float("inf"):
            return -1
        else:
            return ans
        '''

        prev = [1]*(amount+1)

        for t in range(amount + 1):
            if t % coins[0] == 0:
                prev[t] = t // coins[0]
            else:
                prev[t] = float("inf")


        for i in range(1,len(coins)):
            curr = [0]*(amount+1)
            curr[0] = 1
            for j in range(amount+1):
                pick = float("inf")
                if coins[i] <= j:
                    pick = 1 + curr[j-coins[i]]
                notPick = 0 + prev[j]
                curr[j] = min(pick,notPick)

            prev = curr
            
        ans = prev[-1]  
        if ans == float("inf"):
            return -1
        else:
            return ans
                

                

                



        
        
        






























