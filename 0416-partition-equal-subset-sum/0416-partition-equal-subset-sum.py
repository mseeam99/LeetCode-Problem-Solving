class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)

        memo = [bytearray(target + 1) for _ in range(n + 1)]

        def recursion(index, value):
            if value == target:
                return True
            if index == n or value > target:
                return False

            cached = memo[index][value]
            if cached != 0:
                return cached == 2

            pick = recursion(index + 1, value + nums[index])
            if pick:
                memo[index][value] = 2
                return True

            notPick = recursion(index + 1, value)
            memo[index][value] = 2 if notPick else 1
            return notPick

        return recursion(0, 0)
