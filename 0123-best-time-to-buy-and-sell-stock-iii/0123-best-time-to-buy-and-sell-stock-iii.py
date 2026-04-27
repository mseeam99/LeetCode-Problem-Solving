class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        dp = []
        for i in range(len(prices)+1):
            SecondDimension = []
            for j in range(2):
                thirdDimension = []
                for k in range(3):
                    thirdDimension.append(0)
                SecondDimension.append(thirdDimension)
            dp.append(SecondDimension)

        for index in range(len(prices)-1,-1,-1):

            for ifBuyingPossible in range(2):

                for capacity in range(1,3):

                    if ifBuyingPossible == 1:
                        pick = -prices[index] + dp[index+1][0][capacity]
                        notPick = 0 + dp[index+1][1][capacity]
                        result = max(pick,notPick)
                        dp[index][ifBuyingPossible][capacity] = result
                       
                    elif ifBuyingPossible == 0:
                        pick = prices[index] + dp[index+1][1][capacity-1]
                        notPick = 0 + dp[index+1][0][capacity]
                        result = max(pick,notPick)
                        dp[index][ifBuyingPossible][capacity] = result

        return dp[0][1][2]
                       



'''
        def recursion(index, ifBuyingPossible, capacity):
            if dp[index][ifBuyingPossible][capacity] != 0:
                return dp[index][ifBuyingPossible][capacity]
            if (index >= len(prices)) or (capacity <= 0):
                return 0
            if ifBuyingPossible == 1:
                pick = -prices[index] + recursion(index+1,0,capacity)
                notPick = 0 + recursion(index+1,1,capacity)
                result = max(pick,notPick)
                dp[index][ifBuyingPossible][capacity] = result
                return result
            elif ifBuyingPossible == 0:
                pick = prices[index] + recursion(index+1,1,capacity-1)
                notPick = 0 + recursion(index+1,0,capacity)
                result = max(pick,notPick)
                dp[index][ifBuyingPossible][capacity] = result
                return result
        return recursion(0,1,2)
'''