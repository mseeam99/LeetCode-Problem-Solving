class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(array,target):
            leftPointer = 0
            rightPointer = len(array)-1
            while leftPointer <= rightPointer:
                middlePointer = int(leftPointer+(rightPointer-leftPointer)//2)
                if array[middlePointer] == target:
                    return True
                elif array[middlePointer] < target:
                    leftPointer = middlePointer+1
                elif array[middlePointer] > target:
                    rightPointer = middlePointer-1      
        for row in matrix:
            ans = binarySearch(row,target)
            if ans == True:
                return True

        return False
                




                
        