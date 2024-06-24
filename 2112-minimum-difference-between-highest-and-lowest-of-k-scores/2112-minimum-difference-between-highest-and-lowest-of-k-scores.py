class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        
        pointerOne = 0
        pointerTwo = k - 1

        result = float("inf")

        while pointerTwo < len(nums):
            result = min(result , (nums[pointerTwo] - nums[pointerOne]))
            pointerOne+=1
            pointerTwo+=1
            
        return result




     
        

        