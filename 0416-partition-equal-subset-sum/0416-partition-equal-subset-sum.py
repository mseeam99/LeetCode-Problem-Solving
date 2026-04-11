class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2 != 0:
            return False

        target = sum(nums)//2

        dp = []
        for i in range(len(nums)):
            tempArray = [False]*(target+1)
            tempArray[0] = True
            dp.append(tempArray)

        dp[0][0] = True
        
        for i in range(1,len(nums)):
            for j in range(1,target+1):

                notPick    =  dp[i-1][j]
                
                pick = False
                if nums[i] <= j:
                    pick    =  dp[i-1][j-nums[i]]

                dp[i][j] = pick or notPick

        

        return dp[-1][-1]


                 











        

        