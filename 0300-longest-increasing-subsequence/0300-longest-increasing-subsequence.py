class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for i in range(len(nums)+1):
            tempArray = [0] * (len(nums)+1)
            dp.append(tempArray)
        for index in range(len(nums)-1,-1,-1):
            for prevIdx in range(index-1,-2,-1):
                notPick = dp[index + 1][prevIdx+1]
                pick = 0
                if prevIdx == -1 or nums[index] > nums[prevIdx]:
                    pick = 1 + dp[index + 1][index + 1]
                dp[index][prevIdx+1] = max(pick, notPick)
        return dp[0][0]

'''
        def recursion(index, prevIdx):
            if index == len(nums):
                return 0

            prevKey = prevIdx + 1  

            if dp[index][prevKey] != -1:
                return dp[index][prevKey]

            notPick = recursion(index + 1, prevIdx)

            pick = 0
            if prevIdx == -1 or nums[index] > nums[prevIdx]:
                pick = 1 + recursion(index + 1, index)

            dp[index][prevKey] = max(pick, notPick)
            return dp[index][prevKey]

        return recursion(0, -1)
'''