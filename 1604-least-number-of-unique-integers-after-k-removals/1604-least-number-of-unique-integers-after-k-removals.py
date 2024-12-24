class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        theList = []
        hashMap = {}

        for i in range(len(arr)):
            if arr[i] not in hashMap:
                hashMap[arr[i]] = 1
            else:
                hashMap[arr[i]] += 1

        for val,count in hashMap.items():
            theList.append((count,val))

        heapq.heapify(theList)

        for i in range(k):
            t = heapq.heappop(theList)
            if t[0] > 1:
                heapq.heappush(theList,(t[0]-1,t[1]))

        return len(theList)