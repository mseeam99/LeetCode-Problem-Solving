class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        def tryIfItIsValid(middleIndex):
            ops = 0
            for i in range(len(nums)):                
                ops += ceil(nums[i]-1) // middleIndex
                if ops > maxOperations:
                    return False
            return True

        left = 1
        right = max(nums)
        while left <= right:
            middle = left + (right-left) // 2
            if tryIfItIsValid(middle) == True:
                right = middle - 1
            else:
                left = middle + 1
                
        return right + 1


