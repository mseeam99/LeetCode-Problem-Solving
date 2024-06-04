class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        seen        = set()
        duplicate   = set()

        for i in range(len(nums)):
            if nums[i] in seen:
                duplicate.add(nums[i])
            elif nums[i] not in seen:
                seen.add(nums[i])
        
        return list(duplicate)
        



        