class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = 1
            else:
                hashMap[nums[i]] += 1
        count = 0
        maxValue = max(hashMap.values())
        for key,val in hashMap.items():
            if val == maxValue:
                count +=1
        return count*maxValue

        
        