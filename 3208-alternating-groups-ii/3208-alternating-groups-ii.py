class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)

        leftPointer = 0
        rightPointer = 0

        count = 0
        alternatingLength = 0

        while rightPointer < n + k - 1:

            curr = colors[rightPointer % n]
            prev = colors[(rightPointer - 1) % n]

            if rightPointer > 0 and curr != prev:
                alternatingLength += 1
            else:
                alternatingLength = 1

            if rightPointer >= k - 1:
                if alternatingLength >= k:
                    count += 1

            rightPointer += 1

        return count