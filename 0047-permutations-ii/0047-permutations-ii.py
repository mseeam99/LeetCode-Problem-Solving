class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.getPermutation(nums,[],0,result)
        return result

    def getPermutation(self,nums,permArray,idx,result):
        if len(nums) == 0 and permArray not in result:
            result.append(permArray)
            return 

        for i in range(len(nums)):
            newNums = nums[:i] + nums[i+1:]
            idx+=1
            self.getPermutation(newNums,permArray+[nums[i]],idx,result)
