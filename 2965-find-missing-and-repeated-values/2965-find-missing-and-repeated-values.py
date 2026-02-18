class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        start = 1
        end = (len(grid)**2)
        hashMap = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] not in hashMap:
                    hashMap[grid[i][j]] = 1
                else:
                    hashMap[grid[i][j]] += 1

        missing = 0
        for i in range(start,end+1):
            if i not in hashMap:
                missing = i
                break
        
        maxKey,maxVal = 0, 0
        for key,val in hashMap.items():
            if val >= maxVal:
                maxVal = max(maxVal,val)
                maxKey = key

        return [maxKey,missing]
                

