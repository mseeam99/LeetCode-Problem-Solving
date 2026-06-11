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

        lastIndex = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if i + nums[i] >= lastIndex:
                lastIndex = i
        if lastIndex == 0:
            return True
        else:
            return False