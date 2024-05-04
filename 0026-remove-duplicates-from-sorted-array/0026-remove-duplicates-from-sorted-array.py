class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        mySet=set(nums)
        nums[:]=sorted(mySet)
        return len(nums)
        

