class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = {}
        atLeastForMajority = round(len(nums)/2)
        for i in range(len(nums)):
            if nums[i] not in hashMap.keys():
                hashMap[nums[i]] = 1
            elif nums[i] in hashMap.keys():
                value = hashMap[nums[i]]
                value+=1
                hashMap[nums[i]] = value
        key     = list(hashMap.keys())
        values  = list(hashMap.values())
        return key[values.index(max(values))]