class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            hashMap[nums[i]] = i
        for i in range(len(nums)):
            lookingFor = target - nums[i]
            if lookingFor in hashMap and hashMap[lookingFor] != i:
                return [hashMap[lookingFor],i]