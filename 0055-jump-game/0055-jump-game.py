class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        memo = {}
        def recursion(index):
            nonlocal memo
            if index in memo:
                return memo[index]
            if index == len(nums)-1:
                return True
            for i in range(1,nums[index]+1):
                if recursion(index+i) == True:
                    memo[index] = True
                    return True
            memo[index] = False
            return False
        return recursion(0)
        '''

        maxStep = 0
        for i in range(len(nums)):
            if i > maxStep:
                return False
            maxStep = max(maxStep,i+nums[i])
        
        if maxStep >= len(nums)-1:
            return True
        return False
