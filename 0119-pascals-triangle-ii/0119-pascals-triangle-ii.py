class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        array = [1]
        for i in range(1,rowIndex+1):
            returnArray = [0] * (len(array)+1)
            for j in range(len(array)):
                returnArray[j] += array[j]
                returnArray[j+1] += array[j]
            array = returnArray
        return array