class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        one = 0
        two = 0
        for i in range(len(nums)):
            one = (one ^ nums[i]) & (~two)
            two = (two ^ nums[i]) & (~one)
        return one

   