class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:

        subArrayCount = 0

        currentSum = 0
        for i in range(k):
            currentSum += arr[i]

        if currentSum // k >= threshold:
            subArrayCount += 1

        leftPointer = 0
        rightPointer = k

        while rightPointer <= len(arr)-1:

            currentSum += arr[rightPointer]
            currentSum -= arr[leftPointer]

            if currentSum // k >= threshold:
                subArrayCount += 1

            rightPointer += 1
            leftPointer += 1

        return subArrayCount
        