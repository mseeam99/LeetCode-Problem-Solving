class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:


        leftPointer = 0
        rightPointer = 0

        alternatingLength = 0

        count = 0

        while rightPointer < len(colors)+k-1:

            curr = colors[rightPointer % len(colors)]
            prev = colors[(rightPointer-1) % len(colors)]

            if rightPointer > 0 and curr != prev:
                alternatingLength += 1
            else:
                alternatingLength = 1
            

            if rightPointer >= k - 1:
                if alternatingLength >= k:
                    count += 1

            rightPointer += 1

        return count





          