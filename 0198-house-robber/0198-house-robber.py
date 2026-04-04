class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}

        def recursion(index):

            if index >= len(nums):
                return 0
            
            if index in memo:
                return memo[index]
            
            pick = nums[index] + recursion(index+2)
            notPick = 0 + recursion(index+1)

            memo[index] = max(pick,notPick)
            return memo[index]
        
        startAtZero =  recursion(0)
        startAtOne  =  recursion(1)
        return max(startAtZero,startAtOne)

            