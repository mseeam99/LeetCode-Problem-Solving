# [0,1,2,3]
# [2,3,6,7]

# target = 7

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        index = 0
        subArray = []
        finalArray = []
        self.recursion(index,target,candidates,subArray,finalArray)
        return finalArray

    def recursion(self, index, target, givenArray, subArray, finalArray):
        if index == len(givenArray):
            if target == 0:
                finalArray.append(list(subArray))
            return
        
        # pick element
        if givenArray[index] <= target:
            subArray.append(givenArray[index])
            self.recursion(index, target - givenArray[index], givenArray, subArray, finalArray)
            subArray.pop()
        
        # Not pick element 
        self.recursion(index+1, target, givenArray, subArray, finalArray)

        