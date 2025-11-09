class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        hashMap = {}

        for i in range(len(arr)):
            hashMap[arr[i]] = i

        print(hashMap)

        for i in range(len(arr)):
            if (arr[i]*2) in hashMap:
                if hashMap[(arr[i]*2)] != i:
                    return True

        return False
        