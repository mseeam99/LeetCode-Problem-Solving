class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        maxLength = 0
        hashMap = {}
        for i in range(len(nums)):
            hashMap[nums[i]] = 1
        for key,val in hashMap.items():
            currVal = key
            if currVal - 1 not in hashMap:
                nextVal = currVal + 1
                currLength = 1
                while nextVal in hashMap:
                    nextVal += 1
                    currLength += 1
                maxLength = max(maxLength, currLength)
        return maxLength