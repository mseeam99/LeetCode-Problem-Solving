class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums2) > len(nums1):
            nums1, nums2 = nums2, nums1
        myAnswer = []
        for i in range(len(nums2)):
            if nums2[i] in nums1:
                myAnswer.append(nums2[i])
                nums1.remove(nums2[i])
        return myAnswer