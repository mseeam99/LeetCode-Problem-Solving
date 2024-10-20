class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        tempArray = []
        self.getPermutation(nums, tempArray, result)
        return result

    def getPermutation(self, array, current, result):
        if len(array) == 0:
            result.append(current)
            return

        for i in range(len(array)):
            newArray = array[:i] + array[i+1:]  
            self.getPermutation(newArray, current + [array[i]], result)

