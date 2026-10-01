class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] in hashMap:
                return True
            else:
                hashMap[nums[i]] = 1
        return False