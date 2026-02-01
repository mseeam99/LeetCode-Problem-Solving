class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}
        
        def recursion(index,zeroPicked):
            nonlocal nums, memo

            if index > len(nums):
                return 0
            
            if index == len(nums):
                return 0

            if (index,zeroPicked) in memo:
                return memo[(index,zeroPicked)]
            
            pick, notPick = 0,0
            if index == 0:
                zeroPicked = True
            if index == len(nums) - 1 and zeroPicked == True:
                notPick     = 0 + recursion(index+1,zeroPicked)
            else:
                pick        = nums[index] + recursion(index+2,zeroPicked)
            
            if index == 0:
                zeroPicked = False
            if index == len(nums) - 1 and zeroPicked == False:
                pick        = nums[index] + recursion(index+2,zeroPicked)
            else:
                notPick     = 0 + recursion(index+1,zeroPicked)


            maxRobbery  = max(pick,notPick)
            memo[(index,zeroPicked)] = maxRobbery
            return maxRobbery

        return recursion(0,False)
            
        
