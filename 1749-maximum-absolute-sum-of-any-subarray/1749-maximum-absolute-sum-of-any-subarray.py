class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        res = 0
        pos = 0
        neg = 0

        for i in range(len(nums)):

            pos += nums[i]
            if pos < 0:
                pos = 0
            
            neg += nums[i]
            if neg > 0:
                neg = 0

            res = max(res,pos,abs(neg))
            
        return res

