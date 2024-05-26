class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left   = [0] * len(nums)
        right  = [0] * len(nums)
        answer = [0] * len(nums)

        temp = 1
        for i in range(len(nums)):
            left[i] = temp
            temp = temp * nums[i]
        
        temp = 1
        for i in range(len(nums)-1,-1,-1):
            right[i] = temp
            temp = temp * nums[i]

        for i in range(len(nums)):
            answer[i] = left[i] * right[i]
        
        return answer


        