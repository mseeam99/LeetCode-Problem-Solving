class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = 1
            elif nums[i] in hashMap:
                hashMap[nums[i]]+=1

        keys   = list(hashMap.keys())
        values = list(hashMap.values())

        answer = []
        for i in range(k):
            maxValue = max(values)
            maxValueIndex = values.index(maxValue)
            answer.append(keys[maxValueIndex])
            del keys[maxValueIndex]
            del values[maxValueIndex]

        return answer

        
       

        