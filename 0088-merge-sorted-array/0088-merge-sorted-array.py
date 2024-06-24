class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        array = []
        for i in range(m):
            array.append(nums1[i])
        for i in range(n):
            array.append(nums2[i])
        nums1[:] = sorted(array)
        return nums1
        
        