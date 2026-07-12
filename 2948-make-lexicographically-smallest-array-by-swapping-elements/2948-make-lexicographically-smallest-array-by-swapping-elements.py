class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int):

        numsListCopy = sorted(nums)

        groupTrackNumber = 0

        # value -> group
        valueToGroup = {}

        # group -> deque(values)
        groupToValues = {}

        # initialize first group
        valueToGroup[numsListCopy[0]] = 0
        groupToValues[0] = deque([numsListCopy[0]])

        for i in range(1, len(numsListCopy)):

            if abs(numsListCopy[i] - numsListCopy[i-1]) > limit:
                # new group
                groupTrackNumber += 1
                groupToValues[groupTrackNumber] = deque()

            # store which group this value belongs to
            valueToGroup[numsListCopy[i]] = groupTrackNumber

            # store all values in that group
            groupToValues[groupTrackNumber].append(numsListCopy[i])

       
        for i in range(len(nums)):

            currentValue = nums[i]

            # find the group of this value
            groupNumber = valueToGroup[currentValue]

            # take the smallest remaining value from that group
            nums[i] = groupToValues[groupNumber].popleft()

        return nums