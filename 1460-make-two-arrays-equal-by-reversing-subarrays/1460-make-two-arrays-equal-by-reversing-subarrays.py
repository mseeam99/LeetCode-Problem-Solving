class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        
        hashMap = Counter(target)

        for i in range(len(arr)):

            if arr[i] in hashMap:
                hashMap[arr[i]] -= 1
                if hashMap[arr[i]] == 0:
                    del hashMap[arr[i]] 
            else:
                return False

        if len(hashMap) == 0:
            return True
        return False
        