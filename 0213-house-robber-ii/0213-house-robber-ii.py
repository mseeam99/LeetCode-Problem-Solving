class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}

    
        def recursion(index,zeroPicked):

            nonlocal memo

            if (index,zeroPicked) in memo:
                return memo[(index,zeroPicked)]

            if index >= len(nums):
                return 0
        
            if index == len(nums)-1 and zeroPicked == True:
                return 0
            elif index == len(nums)-1 and zeroPicked == False:
                return nums[-1]

            pick = 0
            notPick = 0
            
            if index == 0:
                pick = nums[index] + recursion(index+2, True)
            else:
                pick = nums[index] + recursion(index+2, zeroPicked)
                
            notPick = 0 + recursion(index+1, zeroPicked)
            memo[(index,zeroPicked)] = max(pick, notPick)
            return max(pick, notPick)


        return recursion(0,False)
            



        


        