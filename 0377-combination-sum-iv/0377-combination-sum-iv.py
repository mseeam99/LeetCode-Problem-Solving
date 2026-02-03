class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        memo = {}
        
        def recursion(currentSum):

            nonlocal memo
            
            if currentSum > target:
                return 0

            if currentSum == target:
                return 1

            if currentSum in memo:
                return memo[currentSum]

            ways = 0
            for i in range(len(nums)):
                ways += recursion(currentSum + nums[i])

            memo[currentSum] = ways

            return ways
        
        return recursion(0)

        
        