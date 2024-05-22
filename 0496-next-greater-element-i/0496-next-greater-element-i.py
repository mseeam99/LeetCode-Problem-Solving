class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        pointerOne = 0
        pointerTwo = 0
        while pointerOne<len(nums1):
            tempIndex = nums2.index(nums1[pointerOne])
            pointerTwo = tempIndex+1
            while pointerTwo<len(nums2):
                if nums2[pointerTwo] > nums1[pointerOne]:
                    answer.append(nums2[pointerTwo])
                    break
                elif nums2[pointerTwo] < nums1[pointerOne] and pointerTwo < len(nums2):
                    pointerTwo+=1
            if pointerTwo == len(nums2):
                    answer.append(-1)
            pointerOne+=1
        return answer
                    
                    
        