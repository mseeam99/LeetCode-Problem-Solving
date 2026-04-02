class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:

        hashMap = {}
        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = 1
            else:
                hashMap[nums[i]] += 1
        
        answer = []

        for key, val in hashMap.items():
            if val > 1:
                answer.append(key)

        return answer


        