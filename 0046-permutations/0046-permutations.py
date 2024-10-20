class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        perm = []
        idx = 0
        self.getPermutations(nums,perm,idx,result)
        return result

    def getPermutations(self,array,currentIndexElement,idx,result):
        if len(array) == 0:
            result.append(currentIndexElement)
            return
        
        for i in range(len(array)):
            newArray = array[:i] + array[i+1:]
            idx = idx+1
            self.getPermutations(newArray,currentIndexElement+[array[i]],idx,result)