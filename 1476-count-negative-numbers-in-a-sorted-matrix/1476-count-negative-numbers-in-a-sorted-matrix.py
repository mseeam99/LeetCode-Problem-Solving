class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:

        def binarySearch(array):
            array.sort()
            left = 0
            right = len(array) - 1
            while left <= right:
                middle = left + (right-left) // 2
                if array[middle] <= -1:
                    left = middle + 1
                else:
                    right = middle - 1
            return left

        count = 0
        for i in range(len(grid)):
            count += binarySearch(grid[i])
        return count
        