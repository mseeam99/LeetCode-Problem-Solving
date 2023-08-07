class Solution(object):
    def singleNumber(self, nums):
        nums.sort()
        length = len(nums)
        
        if length==1:
            return nums[0]
        else:
            if nums[0] != nums[1]:
                return nums[0]
            elif nums[length - 1] != nums[length - 2]:
                return nums[length - 1]

            for i in range(1, length - 1):
                if nums[i] != nums[i-1] and nums[i] != nums[i+1]:
                    return nums[i]
             
        
       
        
 