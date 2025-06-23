class Solution:
    def rob(self, nums: List[int]) -> int:
        #Pick or not pick problem (0/1 Knapsack)
        
        memo = {}

        def recursion(index):
            nonlocal nums, memo

            if index >= len(nums):
                return 0
            
            if index in memo:
                return memo[index]

            pick = nums[index] + recursion(index+2)
            notPick = recursion(index+1)

            memo[index] = max(pick,notPick)
            return memo[index]
            
        ans = recursion(0)
        return ans

