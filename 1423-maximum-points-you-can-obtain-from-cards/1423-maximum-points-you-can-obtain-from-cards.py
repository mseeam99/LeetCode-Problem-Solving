class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:

        if k == len(cardPoints):
            return sum(cardPoints)

        totalMaxSum = 0
        summation = sum(cardPoints[0:k])
        totalMaxSum = summation
        headIndex = k-1
        tailIndex = len(cardPoints)-1

        while headIndex >= 0:
            summation -= cardPoints[headIndex]
            summation += cardPoints[tailIndex]
            totalMaxSum = max(totalMaxSum,summation)
            headIndex -= 1
            tailIndex -= 1
        return totalMaxSum
