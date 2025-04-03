class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        
        n = len(nums)
        profitArray1 = [0] * (n - 1)
        profitArray1[0] = nums[0]
        profitArray1[1] = max(nums[0], nums[1])
        for i in range(2, n - 1):
            profitArray1[i] = max(nums[i] + profitArray1[i - 2], profitArray1[i - 1])
        option1 = profitArray1[-1]
        
        profitArray2 = [0] * (n - 1)
        profitArray2[0] = nums[1]
        profitArray2[1] = max(nums[1], nums[2])
        for i in range(2, n - 1):
            profitArray2[i] = max(nums[i + 1] + profitArray2[i - 2], profitArray2[i - 1])
        option2 = profitArray2[-1]
        
        return max(option1, option2)
