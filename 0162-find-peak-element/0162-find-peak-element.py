class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        left = 0
        right = len(nums)-1
        middle = 0

        while left < right:
            middle = left + (right - left) // 2
            if nums[middle] > nums[middle-1] and nums[middle] > nums[middle+1]:
                return middle
            if nums[middle] >= nums[middle+1]:
                right = middle 
            else:
                left = middle + 1

        return left
        