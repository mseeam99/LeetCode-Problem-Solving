class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        minVal = float("inf")
        for i in range(len(nums)-k+1):
            tempDiff = abs(nums[i] - nums[i+k-1])
            minVal = min(minVal,tempDiff)
        return minVal

        
            





        
