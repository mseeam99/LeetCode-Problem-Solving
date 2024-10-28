class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.getSubset(nums, [], 0, result)
        return result

    def getSubset(self, nums, array, index, result):
        result.append(array)
        for i in range(index, len(nums)):
            self.getSubset(nums, array + [nums[i]], i + 1, result)
