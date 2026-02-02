class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        count = Counter(nums)
        elementSet = set()
        memo = {}
        nums = list(set(nums))

        def recursion(index):
            if index >= len(nums):
                return 0

            blocked = nums[index] in elementSet
            key = (index, blocked)
            if key in memo:
                return memo[key]

            pick = 0

            if not blocked:
                elementSet.add(nums[index])
                elementSet.add(nums[index] - 1)
                elementSet.add(nums[index] + 1)

                earn = nums[index] * count[nums[index]]
                pick = earn + recursion(index + 1)

                elementSet.discard(nums[index])
                elementSet.discard(nums[index] - 1)
                elementSet.discard(nums[index] + 1)

            notPick = recursion(index + 1)

            memo[key] = max(pick, notPick)
            return memo[key]

        return recursion(0)
