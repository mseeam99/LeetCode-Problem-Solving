class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}

        def recursion(index):
            nonlocal nums, memo

            if index > len(nums):
                return 0
            
            if index == len(nums):
                return 0

            if index in memo:
                return memo[index]

            pick    = nums[index] + recursion(index+2)
            notPick = 0 + recursion(index+1)
            maxRobbery = max(pick, notPick)
            memo[index] = maxRobbery
            return maxRobbery
        
        return recursion(0)
            


            
        