class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        hashMap = {}
        for i in range(len(arr)):
            if arr[i] not in hashMap:
                hashMap[arr[i]] = 1
            else:
                hashMap[arr[i]] += 1
        
        mySet = set()
        for key,val in hashMap.items():
            if val in mySet:
                return False
            mySet.add(val)
            
        return True



            