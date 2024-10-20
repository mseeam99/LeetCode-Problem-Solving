class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.getPermutations(nums,[],result)
        return result

    def getPermutations(self,array,currentIndexElement,result):
        if len(array) == 0:
            result.append(currentIndexElement)
            return
        
        for i in range(len(array)):
            newArray = array[:i] + array[i+1:]
            self.getPermutations(newArray,currentIndexElement+[array[i]],result)