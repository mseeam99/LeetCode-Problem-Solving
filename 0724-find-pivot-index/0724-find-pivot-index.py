class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pointerOne = 0
        while pointerOne < len(nums):
            if sum(nums[:pointerOne]) == sum(nums[pointerOne+1:]):
                return pointerOne
            else:
                pointerOne+=1
        return -1