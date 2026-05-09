class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        
        colors.extend(colors[:k - 1])

        prevColor = colors[0]
        rightPointer = 1

        shuffleLength = 1
        totalCountGroup = 0

        while rightPointer <= len(colors)-1:

            currColor = colors[rightPointer]

            if currColor != prevColor:
                shuffleLength += 1
            else:
                shuffleLength = 1

            prevColor = colors[rightPointer]

            if shuffleLength >= k:
                totalCountGroup += 1

            rightPointer += 1
        
        return totalCountGroup

        