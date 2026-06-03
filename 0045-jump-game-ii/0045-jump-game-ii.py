class Solution:
    def jump(self, nums: List[int]) -> int:

        leftPointer = 0
        rightPointer = 0

        jumps = 0

        while rightPointer < len(nums)-1:
            farthest = 0
            for i in range(leftPointer,rightPointer+1):
                farthest = max(farthest,i+nums[i])
            leftPointer = rightPointer + 1
            rightPointer = farthest
            jumps += 1

        
        return jumps
