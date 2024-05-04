import statistics

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        newArray = []

        for i in range(len(nums1)):
            newArray.append(nums1[i])
        
        for j in range(len(nums2)):
            newArray.append(nums2[j])

        newArray = sorted(newArray)

        answer =  statistics.median(newArray)

        return answer
