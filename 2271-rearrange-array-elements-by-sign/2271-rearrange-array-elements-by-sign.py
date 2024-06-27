class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positiveArray = []
        negativeArray = []
        for i in range(len(nums)):
            if nums[i] >= 0 :
                positiveArray.append(nums[i])
            else:
                negativeArray.append(nums[i])

        answer = []
        iteration = len(nums)//2
        for i in range(iteration):
            answer.append(positiveArray[i])
            answer.append(negativeArray[i])
        nums[:] = answer
        return nums




        


        