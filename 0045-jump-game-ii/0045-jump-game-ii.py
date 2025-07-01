class Solution:
    def jump(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0

        jumps = 0
        current_end = 0
        farthest = 0
        i = 0

        while i < len(nums) - 1:
            # Within the current jump range, find the farthest we can go
            while i <= current_end:
                farthest = max(farthest, i + nums[i])
                i += 1
                if farthest >= len(nums) - 1:
                    return jumps + 1
            # Move to the next jump range
            jumps += 1
            current_end = farthest

        return jumps
