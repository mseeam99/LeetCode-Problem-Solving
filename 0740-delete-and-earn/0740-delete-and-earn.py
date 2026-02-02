from typing import List
from collections import Counter

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0

        count = Counter(nums)
        values = sorted(count.keys())   # unique sorted values

        elementSet = set()
        memo = {}

        def recursion(index: int, prevPicked: int) -> int:
            if index >= len(values):
                return 0

            key = (index, prevPicked)
            if key in memo:
                return memo[key]

            v = values[index]

            # not pick
            notPick = recursion(index + 1, 0)

            # pick (only if not blocked)
            pick = 0

            blocked = False
            if prevPicked == 1 and index > 0 and values[index] == values[index - 1] + 1:
                blocked = True

            if (not blocked) and (v not in elementSet):
                # your style
                elementSet.add(v)
                elementSet.add(v - 1)
                elementSet.add(v + 1)

                earn = v * count[v]
                pick = earn + recursion(index + 1, 1)

                # backtrack EXACTLY what you added
                if elementSet:
                    elementSet.remove(v)
                if elementSet:
                    elementSet.remove(v - 1)
                if elementSet:
                    elementSet.remove(v + 1)

            memo[key] = max(pick, notPick)
            return memo[key]

        return recursion(0, 0)
