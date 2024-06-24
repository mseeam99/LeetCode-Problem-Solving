class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        count   = 1
        pointer = 1

        while pointer < len(nums):
            if nums[pointer-1] == nums[pointer] and count != 2:
                count+=1
                pointer+=1
            elif nums[pointer-1] == nums[pointer] and count == 2:
                del nums[pointer]
            elif nums[pointer-1] != nums[pointer]:
                count=1
                pointer+=1

        return len(nums)
        