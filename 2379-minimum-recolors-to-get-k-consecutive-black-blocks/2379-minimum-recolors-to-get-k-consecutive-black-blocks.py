class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whiteCount = 0
        for i in range(k):
            if blocks[i] == "W":
                whiteCount += 1
        minWhite = whiteCount
        rightPointer = k
        leftPointer = 0
        while rightPointer <= len(blocks)-1:
            if blocks[rightPointer] == "W":
                whiteCount += 1
            if blocks[leftPointer] == "W":
                whiteCount -= 1
            minWhite = min(minWhite,whiteCount)
            rightPointer += 1
            leftPointer += 1
        return minWhite

            
