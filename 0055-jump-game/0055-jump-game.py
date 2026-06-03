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

        maxJump = 0
        for i in range(len(nums)):
            if maxJump < i:
                return False
            maxJump = max(maxJump,i+nums[i])
            if maxJump >= len(nums)-1:
                return True
        return False







        
        