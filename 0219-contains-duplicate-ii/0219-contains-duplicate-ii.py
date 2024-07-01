class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashMap = {}
        answerAsBoolean = False
        for i in range(len(nums)):
            if nums[i] in hashMap.keys():
                value = hashMap[nums[i]]
                if i != value and abs(i-value) <= k:
                    answerAsBoolean = True
                hashMap[nums[i]] = i
            else:
                hashMap[nums[i]] = i
        return answerAsBoolean





        