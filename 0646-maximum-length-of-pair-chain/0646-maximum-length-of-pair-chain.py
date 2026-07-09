class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        lastValue = float("-inf")
        maxLength = 0
        for i in range(len(pairs)):
            pair = pairs[i]
            if pair[0] > lastValue:
                lastValue = pair[1]
                maxLength += 1
        return maxLength
