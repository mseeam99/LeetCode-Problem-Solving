class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            stringVersion = str(nums[i])
            if len(stringVersion) == 1:
                if i == nums[i]:
                    return i
            else:
                summation = 0
                for j in range(len(stringVersion)):
                    summation += int(stringVersion[j])
                if summation == i:
                    return i
        return -1

        