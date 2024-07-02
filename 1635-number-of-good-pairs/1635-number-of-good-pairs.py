class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        pointerOne = 0
        pointerTwo = pointerOne + 1

        count = 0

        while pointerOne < len(nums)-1:
            if  nums[pointerOne] == nums[pointerTwo]:
                count+=1
                pointerTwo+=1
            else:
                pointerTwo+=1
            
            if pointerTwo == len(nums):
                pointerOne+=1
                pointerTwo = pointerOne + 1

        return count



        



        