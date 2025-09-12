class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:

        if p == 0: return 0
            
        def linear(threshold):
            index = 0
            totalPairCount = 0
            while index < len(nums)-1:
                if abs(nums[index]-nums[index+1]) <= threshold:
                    totalPairCount+=1
                    index+=2
                else:
                    index+=1
            
                if totalPairCount == p:
                    return True
            return False

        nums.sort()
        left = 0
        right = max(nums)
        result = max(nums)
        while left <= right:
            middle = left + (right-left) // 2
            if linear(middle) == True:
                result = middle
                right = middle - 1
            else:
                left = middle + 1
        return result




        