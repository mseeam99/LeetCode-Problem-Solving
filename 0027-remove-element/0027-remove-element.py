class Solution(object):
    def removeElement(self, nums, val):
        index = 0
        while index < len(nums):
            if nums[index] == val:
                del nums[index]
                index + 1
            else:
                index = index + 1
        


