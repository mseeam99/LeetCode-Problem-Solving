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
        totalMax = summation
        startDeletingFromIndex = k-1
        rightmostIndex = len(cardPoints)-1
        for i in range(k):
            summation -= cardPoints[startDeletingFromIndex]
            startDeletingFromIndex-=1
            summation += cardPoints[rightmostIndex]
            rightmostIndex-=1
            totalMax = max(totalMax,summation)
        return totalMax




       