class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr = arr[::-1]
        result = []
        maximumElement = -1
        for i in range(len(arr)):
            result.append(maximumElement)
            if arr[i] > maximumElement:
                maximumElement = arr[i]
        return result[::-1]




        


        