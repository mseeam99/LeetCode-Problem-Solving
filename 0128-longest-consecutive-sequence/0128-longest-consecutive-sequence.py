from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mySet = set(nums)  # Convert to set to remove duplicates and allow O(1) lookup
        maxValue = 0
        
        for num in mySet:  # Iterate directly over the set
            if num - 1 not in mySet:  # Start counting only if it's the start of a sequence
                count = 0
                while num + count in mySet:  # Continue the sequence
                    count += 1
                maxValue = max(maxValue, count)  # Update the max sequence length
        
        return maxValue
