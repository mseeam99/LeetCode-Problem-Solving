class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxval  = nums[0]
        current = nums[0]
        for i in range(1,len(nums)):
            current = max(nums[i],current+nums[i])
            if current <= 0 :
                current = nums[i]
            maxval  = max(maxval,current)
        return maxval
        