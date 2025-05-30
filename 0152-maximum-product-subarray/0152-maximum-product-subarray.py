class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        maxValue    = 1         
        minValue    = 1        
        answer      = max(nums)

        for i in range(len(nums)):
            if nums[i] == 0:
                maxValue, minValue = 1, 1  
                continue
            
            temp_max = maxValue * nums[i]
            temp_min = minValue * nums[i]

            maxValue = max(nums[i], temp_max, temp_min)
            minValue = min(nums[i], temp_max, temp_min)

            answer = max(answer, maxValue)

        return answer
