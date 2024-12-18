class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums) 
        maxValue = 0
        for num in mySet:  
            if num - 1 not in mySet: 
                count = 0
                while num + count in mySet:  
                    count += 1
                maxValue = max(maxValue, count) 
        return maxValue