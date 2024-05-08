class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        myAnswer = set()
        for i in range(len(nums2)):
            if nums2[i] in nums1:
                myAnswer.add((nums2[i]))
        myAnswer = list(myAnswer)
        return myAnswer