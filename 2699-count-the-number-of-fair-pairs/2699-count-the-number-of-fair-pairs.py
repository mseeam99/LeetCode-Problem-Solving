class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums)):
            l = self.bisect_left_manual(nums, lower - nums[i], i + 1, len(nums))
            r = self.bisect_right_manual(nums, upper - nums[i], i + 1, len(nums))
            count += r - l
        return count

    def bisect_left_manual(self, a, x, lo, hi):
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        return lo
    
    def bisect_right_manual(self, a, x, lo, hi):
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] <= x:
                lo = mid + 1
            else:
                hi = mid
        return lo