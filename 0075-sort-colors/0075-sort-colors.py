class Solution:
    def sortColors(self, nums: List[int]) -> None:
        if len(nums) == 1:
            return nums
        middle = len(nums)//2
        left   = self.sortColors(nums[:middle])
        right  = self.sortColors(nums[middle:])
        answer = self.merge(left,right)
        nums[:] = answer
        return nums

    def merge(self,left,right):
        result = []
        pointerOne = 0
        pointerTwo = 0
        while pointerOne < len(left) and pointerTwo < len(right):
            if left[pointerOne] <= right[pointerTwo]:
                result.append(left[pointerOne])
                pointerOne+=1
            elif right[pointerTwo] < left[pointerOne]:
                result.append(right[pointerTwo])
                pointerTwo+=1
        if pointerOne < len(left):
            result.extend(left[pointerOne:])
        if pointerTwo < len(right):
            result.extend(right[pointerTwo:])
        return result
    

    





       