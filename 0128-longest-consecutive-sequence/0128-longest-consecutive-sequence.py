class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for i in range(len(nums)):
            if (nums[i] - 1 ) not in numSet:
                temp = 0
                while (nums[i] + temp) in numSet:
                    temp += 1
                longest = max(longest,temp)
        return longest

        