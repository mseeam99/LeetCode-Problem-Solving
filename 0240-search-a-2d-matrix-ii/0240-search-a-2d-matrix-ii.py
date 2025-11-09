class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binarySearch(array,target):
            left = 0
            right = len(array)-1
            while left <= right:
                middle = left + (right-left) // 2
                if array[middle] == target:
                    return True
                elif array[middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1
            return False
                    
        answer = False
        for i in matrix:
            currentRow = i
            if currentRow[0] <= target and currentRow[len(currentRow)-1] >= target:
                answer = binarySearch(currentRow,target)
                if answer == True:
                    break
        return answer
                




        