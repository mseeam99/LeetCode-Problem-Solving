class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        if len(nums) == 1:
            return nums[0]
        if nums[0] != nums[0+1]:
            return nums[0]
        if nums[len(nums)-1] != nums[len(nums)-2]:
            return nums[len(nums)-1]
        for i in range(1,len(nums)-1):
            if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                return nums[i]
