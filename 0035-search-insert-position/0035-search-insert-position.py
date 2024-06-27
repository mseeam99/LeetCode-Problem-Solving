class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
       
        if len(nums) == 1 and target == 0:
            return 0
        
        if len(nums) == 1 and target == 1:
            return 0

        answer = 0
        for i in range(len(nums)):
            if target <= nums[i] :
                answer =  i
                return answer
           
        if answer == 0:
            return len(nums)
        return answer

        


        