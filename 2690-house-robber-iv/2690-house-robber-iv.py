class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def linear(capacity):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= capacity:
                    i+=2
                    count+=1
                else:
                    i+=1
                if count == k:
                    break
            return count == k  
        left  = min(nums)
        right = max(nums)
        result = 0
        while left <= right:
            middle = left + (right-left) // 2
            if linear(middle) == True:
                result = middle
                right = middle - 1
            else:
                left = middle + 1
        return result
