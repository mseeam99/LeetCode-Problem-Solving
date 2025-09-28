class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if len(nums) == 0:
            return [-1,-1]

        def bisectLeft(nums,target):
            left = 0
            right = len(nums)-1
            while left <= right:
                middle = left + (right-left) // 2
                if nums[middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1
            return left

        def bisectRight(nums,target):
            left = 0
            right = len(nums)-1
            while left <= right:
                middle = left + (right-left) // 2
                if nums[middle] <= target:
                    left = middle + 1
                else:
                    right = middle - 1
            return left

        leftIndex = bisectLeft(nums,target)
        rightIndex = bisectRight(nums,target) - 1
        found = False
        for i in range(leftIndex,rightIndex+1):
            if nums[i] == target:
                found = True
                break
        if found == True:
            return [leftIndex,rightIndex]
        else:
            return [-1,-1]

        