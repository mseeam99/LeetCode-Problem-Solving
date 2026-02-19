class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashMap = {}
        answerMap = []
        for i in range(len(nums2)):
            hashMap[nums2[i]] = i
        for i in range(len(nums1)):
            answerMap.append(hashMap[nums1[i]]) 
        return answerMap
        

        