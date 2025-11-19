class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        left = 0
        right = len(arr) - 1
        
        while left <= right:

            middle = left + (right-left) // 2

            if arr[middle-1] < arr[middle] and arr[middle] > arr[middle+1]:
                return middle
            if arr[middle-1] > arr[middle]: # Decreasing
                right = middle 
            else:          
                left = middle + 1
         



