class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        if len(arr) == 1:
            return 1

        maxLength = 1

        def compare(left,right):
            if left > right:    #left bigger
                return -1
            elif left < right:  #right bigger
                return 1
            else:
                return 0
        

        leftPointer = 0
        for rightPointer in range(1, len(arr)):

            curr = compare(arr[rightPointer], arr[rightPointer - 1])

            if curr == 0:
                leftPointer = rightPointer
                continue

            if rightPointer == 1:
                maxLength = max(maxLength, 2)
                continue

            prev = compare(arr[rightPointer - 1], arr[rightPointer - 2])

            if curr * prev == -1:
                maxLength = max(maxLength, rightPointer - leftPointer + 1)
            else:
                leftPointer = rightPointer - 1
                maxLength = max(maxLength, 2)

        return maxLength