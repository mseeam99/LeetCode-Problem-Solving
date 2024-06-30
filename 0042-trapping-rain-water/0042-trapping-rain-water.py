class Solution:
    def trap(self, height: List[int]) -> int:

        leftPointer  = 0
        rightPointer = len(height) - 1

        leftValue  = height[leftPointer]
        rightValue = height[rightPointer]

        water_trapped = 0
        
        while leftPointer < rightPointer:
            if leftValue < rightValue:
                leftPointer += 1
                leftValue = max(leftValue, height[leftPointer])
                water_trapped += max(0, leftValue - height[leftPointer])
            else:
                rightPointer -= 1
                rightValue = max(rightValue, height[rightPointer])
                water_trapped += max(0, rightValue - height[rightPointer])
        
        return water_trapped







