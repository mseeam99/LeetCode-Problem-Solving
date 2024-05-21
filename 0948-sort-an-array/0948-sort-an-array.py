class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:  return nums
        middle = len(nums) // 2
        left         = self.sortArray(nums[:middle])
        right        = self.sortArray(nums[middle:])
        sortedAnswer = self.merge(left,right)
        return sortedAnswer

    def merge(self,left,right):
        result = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        if i < len(left):
            result.extend(left[i:])
        if j < len(right):
            result.extend(right[j:])
        return result

        