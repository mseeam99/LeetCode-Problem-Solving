class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:

        hashMap = {}
        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = 1
            else:
                hashMap[nums[i]]+=1

        targetLength = len(nums) // 2

        for key,val in hashMap.items():
            if val == targetLength:
                return key
        