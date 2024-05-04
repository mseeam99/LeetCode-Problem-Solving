class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
        for index, number in enumerate(nums):
            if number in hashmap:
                return [hashmap[number], index]
            else:
                tempDifference = target - number
                hashmap[tempDifference] = index
