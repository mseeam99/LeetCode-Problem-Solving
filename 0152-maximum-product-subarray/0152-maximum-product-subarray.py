class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            if 0 in nums:
                return max(nums)
            return max(nums[0] * nums[1], max(nums))

        dp_max = [0] * len(nums)
        dp_min = [0] * len(nums)

        dp_max[0] = nums[0]
        dp_min[0] = nums[0]

        print("dp_max:", dp_max)
        print("dp_min:", dp_min)

        for i in range(1, len(nums)):
            dp_max[i] = max(nums[i], dp_max[i-1] * nums[i], dp_min[i-1] * nums[i])
            dp_min[i] = min(nums[i], dp_max[i-1] * nums[i], dp_min[i-1] * nums[i])

        print("dp_max:", dp_max)
        print("dp_min:", dp_min)

        return max(dp_max)
