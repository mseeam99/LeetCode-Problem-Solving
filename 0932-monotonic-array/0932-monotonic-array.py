class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        if nums[0] <= nums[len(nums)-1]:
            for i in range(len(nums)-1):
                if not (nums[i] <= nums[i+1]):
                    return False
            return True

        if nums[0] > nums[len(nums)-1]:
            for i in range(len(nums)-1):
                if not (nums[i] >= nums[i+1]):
                    return False
            return True


            