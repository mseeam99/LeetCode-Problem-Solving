class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:

        nums.sort()
        leftPointer = 0
        rightPointer = len(nums) - 1
        answer = 0 

        while leftPointer <= rightPointer:
            if nums[leftPointer] + nums[rightPointer] <= target:
                answer += pow(2,rightPointer - leftPointer)
                leftPointer+=1
            elif nums[leftPointer] + nums[rightPointer] > target:
                rightPointer-=1
        
        modValue = (pow(10,9))+7
        answer =  (answer % modValue)
        return answer

        
        