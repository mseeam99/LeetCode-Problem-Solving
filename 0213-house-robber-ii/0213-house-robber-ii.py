class Solution:
    def rob(self, nums: List[int]) -> int:

        '''
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
        '''
        if len(nums) == 1:
            return nums[0]
        dp1 = [0]*(len(nums)+1)
        dp2 = [0]*(len(nums)+1)
        for i in range(len(nums)):
            pick,notPick = 0,0
            if i != len(nums)-1:
                pick    = nums[i] + dp1[i-2]
            notPick = 0 + dp1[i-1]
            maxValue = max(pick,notPick)
            dp1[i] = maxValue
        for i in range(1,len(nums)):
            pick,notPick = 0,0
            pick    = nums[i] + dp2[i-2]
            notPick = 0 + dp2[i-1]
            maxValue = max(pick,notPick)
            dp2[i] = maxValue
        return max(dp1[len(nums)-1],dp2[len(nums)-1])
            



        


        