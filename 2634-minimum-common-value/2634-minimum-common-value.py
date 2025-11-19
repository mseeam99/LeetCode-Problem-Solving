class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        hashMap = {}
        ans = float("inf")
        for i in range(len(nums1)):
            hashMap[nums1[i]] = i
        for i in range(len(nums2)):
            if nums2[i] in hashMap:
                ans = min(ans,nums2[i])
        return -1 if ans == float("inf") else ans

        