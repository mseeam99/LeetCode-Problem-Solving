class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        for i in range(len(nums)+1):
            tempArray = [0] * (len(nums)+1)
            dp.append(tempArray)
        
        nextArr = [0]*(len(nums)+1)
        currArr = [0]*(len(nums)+1)

        for index in range(len(nums)-1,-1,-1):
            for prevIdx in range(index-1,-2,-1):
                notPick = nextArr[prevIdx+1]
                pick = 0
                if prevIdx == -1 or nums[index] > nums[prevIdx]:
                    pick = 1 + nextArr[index + 1]
                currArr[prevIdx+1] = max(pick, notPick)
            nextArr = currArr 
        return nextArr[0]

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