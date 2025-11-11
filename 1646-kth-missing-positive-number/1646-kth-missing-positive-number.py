class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        mySet = set()
        for i in range(len(arr)):
            mySet.add(arr[i])
        totalLength = max(arr)+k
        missingCount = 0
        for i in range(1,totalLength+1):
            if i not in mySet:
                missingCount+=1
                if missingCount == k:
                    return i


        