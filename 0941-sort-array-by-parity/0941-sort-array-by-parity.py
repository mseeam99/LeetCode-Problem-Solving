class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        answer = []

        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                answer.append(nums[i])
        
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                answer.append(nums[i])

        return answer

        

        