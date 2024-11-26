class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        array = []
        for i in range(len(arr)):
            if arr[i] == 0:
                array.append(0)
                array.append(0)
            else:
                array.append(arr[i])
        arr[:] = array[:len(arr)]
        