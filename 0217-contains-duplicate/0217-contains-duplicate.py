class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        newList = list(set(nums))
        answer = True if len(nums) != len(newList) else False
        return answer