class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:

        if len(nums) == 0:
            return 0
        
        hashMap = {}
        for i in range(len(nums)):
            hashMap[nums[i]] = 1

        nums.sort()

        for i in range(len(nums)):


            if nums[i]-1 in hashMap:
                hashMap[nums[i]] = hashMap[nums[i]-1]+1

        print(hashMap)
            

        maxVal = float("-inf")

        for key, val in hashMap.items():
            if val >= maxVal:
                maxVal = val
        
        return maxVal
            

        