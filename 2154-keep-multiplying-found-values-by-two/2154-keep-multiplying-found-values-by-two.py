class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:

        hashMap = {}
        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = 1
            else:
                hashMap[nums[i]] += 1

        booleanRunning = True
        while booleanRunning:
            if original not in hashMap:
                booleanRunning = False
                break
            original = original * 2

        return original 