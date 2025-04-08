class Solution:
    def canJump(self, nums: List[int]) -> bool:

        leftPointer  = 0
        prevMaxValueFound, maxValueFound = 0, 0
        maxIndexAssociatedWithValue = 0

        while leftPointer < len(nums):

            if (leftPointer + nums[leftPointer]) >= len(nums)-1:
                return True

            maxIndexAssociatedWithValue = leftPointer

            for i in range(leftPointer+1,min(leftPointer+nums[leftPointer]+1,len(nums))):
            
                candidate = i + nums[i]  # total reach from index i
                if candidate > prevMaxValueFound:
                    prevMaxValueFound = candidate
                    maxValueFound = nums[i]
                    maxIndexAssociatedWithValue = i
            
            print(maxValueFound)
            nums[leftPointer] = maxValueFound
            
            if maxIndexAssociatedWithValue == leftPointer:
                return False

            leftPointer = maxIndexAssociatedWithValue
            prevMaxValueFound, maxValueFound = 0, 0
            maxIndexAssociatedWithValue = 0

        return False

        
            


