class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxValue = 1
        minValue = 1
        answer = max(nums)  
        
        for num in nums:
            if num == 0:
                maxValue, minValue = 1, 1  
            
            temp_max = maxValue * num
            temp_min = minValue * num

            maxValue = max(num, temp_max, temp_min)
            minValue = min(num, temp_max, temp_min)

            answer = max(answer, maxValue)

        return answer
