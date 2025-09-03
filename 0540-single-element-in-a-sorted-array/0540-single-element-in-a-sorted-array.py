class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]

        left = 1
        right = len(nums) - 2
        middle = 0

        while left <= right:

            middle = left + (right - left) // 2

            if nums[middle-1] != nums[middle] and nums[middle] != nums[middle+1]:
                return nums[middle]

            if (middle % 2 == 1 and nums[middle] == nums[middle-1]) or (middle % 2 == 0 and nums[middle] == nums[middle+1]):
                #pattern good
                left = middle + 1

            elif (middle % 2 == 1 and nums[middle] != nums[middle-1]) or (middle % 2 == 0 and nums[middle] == nums[middle-1]):
                #pattern bad
                right = middle - 1
          
        return nums[left]






        