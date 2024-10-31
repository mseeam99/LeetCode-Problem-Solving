class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        hashMap = {}

        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = 0
            else:
                continue
        
        track = 0

        for i in range(len(nums)):
            if track not in hashMap:
                return track
            else:
                track+=1

        return track

        
        




        