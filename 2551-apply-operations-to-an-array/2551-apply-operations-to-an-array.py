class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0

        answer = []
        count = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                answer.append(nums[i])

        for i in range(count):
            answer.append(0)

        return answer
            
        

        