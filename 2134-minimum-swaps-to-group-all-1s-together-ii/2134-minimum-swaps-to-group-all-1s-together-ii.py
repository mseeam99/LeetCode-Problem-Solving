class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        oneCount = nums.count(1)
        if oneCount <= 1:
            return 0
        data = nums+nums
        leftPointer = 0
        rightPointer = oneCount
        globalMinSwapNeeded = float("inf")
        curretSwapNeeded = 0
        for i in range(leftPointer,rightPointer):
            if data[i] == 0:
                curretSwapNeeded += 1
        globalMinSwapNeeded = min(globalMinSwapNeeded,curretSwapNeeded)
        while rightPointer < len(data):
            if data[rightPointer] == 0:
                curretSwapNeeded += 1    
            if data[leftPointer] == 0:
                curretSwapNeeded -= 1
            leftPointer += 1
            rightPointer += 1
            globalMinSwapNeeded = min(globalMinSwapNeeded, curretSwapNeeded)
        return globalMinSwapNeeded