class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:

        def binarySearch(val):
            left = 0
            right = len(bobSizes)-1
            while left <= right:
                middle = left + (right-left) // 2
                if bobSizes[middle] == val:
                    return True
                elif bobSizes[middle] < val:
                    left = middle + 1
                else:
                    right = middle - 1
            return False

        totalCandy = sum(aliceSizes) + sum(bobSizes)
        oneSideShouldHave = totalCandy // 2

        aliceSizes.sort()
        bobSizes.sort()

        for i in range(len(aliceSizes)):
            need = (oneSideShouldHave - sum(aliceSizes)) + aliceSizes[i]
            if binarySearch(need) == True:
                return [aliceSizes[i],need]
        

        
        