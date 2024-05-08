class Solution(object):
    def twoSum(self, nums, target):
        hashMap = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hashMap:
                return [hashMap[difference], i]
            else:
                hashMap[nums[i]] = i