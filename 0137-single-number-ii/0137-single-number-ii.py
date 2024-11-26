class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        hashMap = {}

        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = 1
            else:
                hashMap[nums[i]] += 1

        keys = list(hashMap.keys())
        values = list(hashMap.values())

        for i in range(len(values)):
            if values[i] == 1:
                return keys[i]