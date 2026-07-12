class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int):

        numsListCopy = sorted(nums)
        groupTrackNumber = 0
        valueToGroup = {}
        groupToValues = {}
        valueToGroup[numsListCopy[0]] = 0
        groupToValues[0] = deque([numsListCopy[0]])

        for i in range(1, len(numsListCopy)):
            if abs(numsListCopy[i] - numsListCopy[i-1]) > limit:
                groupTrackNumber += 1
                groupToValues[groupTrackNumber] = deque()
            valueToGroup[numsListCopy[i]] = groupTrackNumber
            groupToValues[groupTrackNumber].append(numsListCopy[i])

        for i in range(len(nums)):
            currentValue = nums[i]
            groupNumber = valueToGroup[currentValue]
            nums[i] = groupToValues[groupNumber].popleft()
        return nums