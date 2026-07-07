class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        '''
        if k == len(cardPoints):
            return sum(cardPoints)
        leftValues = cardPoints[:k]
        rightValues = cardPoints[-k:]
        maxSum = 0
        for i in range(k + 1):
            leftSum = sum(leftValues[:i])
            rightCount = k - i
            rightSum = 0
            if rightCount > 0:
                rightSum = sum(rightValues[-rightCount:]) 
            else:
                rightSum = 0
            maxSum = max(maxSum, leftSum + rightSum)
        return maxSum
        '''

        if k == len(cardPoints):
            return sum(cardPoints)        
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
        
