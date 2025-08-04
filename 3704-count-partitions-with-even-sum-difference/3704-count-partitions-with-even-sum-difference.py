class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        answerCount = 0
        for i in range(len(nums)-1):
            leftPart  = sum(nums[:i+1])
            rightPart = sum(nums[i+1:])
            if abs(rightPart - leftPart) % 2 == 0:
                answerCount+=1
        return answerCount
        