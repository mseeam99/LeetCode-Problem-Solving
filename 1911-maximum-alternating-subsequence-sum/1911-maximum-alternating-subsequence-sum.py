class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        maxValue = float('-inf')

        memo = {}

        def recursion(index,positive):
            
            if index >= len(nums):
                return 0

            if (index,positive) in memo:
                return memo[(index,positive)]

            notPick = recursion(index + 1, positive)
        
            if positive == True:
                pick = +nums[index] + recursion(index+1,False)
            elif positive == False:
                pick = -nums[index] + recursion(index+1,True)

            memo[(index,positive)] = max(pick,notPick)
            return max(pick,notPick)

            
             
              
            
           

           
        return recursion(0,True)

       