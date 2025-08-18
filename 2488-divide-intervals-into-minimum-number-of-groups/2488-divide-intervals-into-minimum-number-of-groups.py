class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        startArray = []
        endArray = []
        for i in range(len(intervals)):
            startArray.append(intervals[i][0])
            endArray.append(intervals[i][1])
        startArray.sort()
        endArray.sort()
        i , j = 0, 0
        maxLength = float("-inf")
        count = 0
        while i < len(startArray):
            if startArray[i] <= endArray[j]:
                count+=1
                i+=1
            else:
                count-=1
                j+=1
            maxLength = max(maxLength,count)
        return maxLength
        