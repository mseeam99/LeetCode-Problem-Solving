class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:

        hashMap = {}

        for i in range(len(nums1)):
            hashMap[nums1[i]] = 1
            
        for i in range(len(nums2)):
            hashMap[nums2[i]] = 1
            
        for i in range(len(nums3)):
            hashMap[nums3[i]] = 1
        
        nums1 = set(nums1)
        nums2 = set(nums2)
        nums3 = set(nums3)
        
        answer = []

        for key,val in hashMap.items():
            if (key in nums1 and key in nums2) or (key in nums2 and key in nums3) or (key in nums1 and key in nums3):
                answer.append(key)

        return answer