class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        resultArrayLeftToRight = [1] * len(nums)
        resultArrayLeftToRight[0] = 1

        for i in range(1,len(nums)):
            resultArrayLeftToRight[i] = resultArrayLeftToRight[i-1] * nums[i-1]
        
        resultArrayRightToLeft = [1] * len(nums)

        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                continue
            resultArrayRightToLeft[i] = resultArrayRightToLeft[i+1] * nums[i+1]

        answer = [0]*len(nums)
        for i in range(len(resultArrayLeftToRight)):
            answer[i] = resultArrayLeftToRight[i] * resultArrayRightToLeft[i]

        return answer