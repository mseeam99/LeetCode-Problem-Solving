class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicateValueIs = 0
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = 1
            else:
                hashMap[nums[i]] += 1
                duplicateValueIs = nums[i]

        for i in range(1,len(nums)+1):
            if i not in hashMap:
                return [duplicateValueIs,i]


        