class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        answer = []
        pointerOne = 0
        while pointerOne < len(nums):
            start = nums[pointerOne]
            while pointerOne < len(nums)-1 and nums[pointerOne]+1 == nums[pointerOne+1]:
                pointerOne += 1
            if start != nums[pointerOne]:
                answer.append(str(start) + "->" + str(nums[pointerOne]))
            else:
                answer.append(str(start))
            pointerOne += 1
        return answer
