class Solution:
    def maxArea(self, height: List[int]) -> int:
        leftPointer = 0
        rightPointer = len(height) - 1
        answer = []
        while leftPointer < rightPointer:
            distance = rightPointer - leftPointer
            tempMinValue = min(height[leftPointer],height[rightPointer])
            tempValue = tempMinValue * distance
            answer.append(tempValue)
            if height[leftPointer] < height[rightPointer]:
                leftPointer+=1
            elif height[leftPointer] >= height[rightPointer]:
                rightPointer-=1
        return max(answer)




