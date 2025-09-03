class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = left + (right - left) // 2
            if (middle == 0 or nums[middle] > nums[middle-1]) and \
            (middle == len(nums)-1 or nums[middle] > nums[middle+1]):
                return middle
            elif middle < len(nums)-1 and nums[middle] < nums[middle+1]:
                left = middle + 1
            else:
                right = middle - 1
