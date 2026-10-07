class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:

        leftPointer = 0
        rightPointer = len(nums)-1

        while leftPointer <= rightPointer:
            if nums[leftPointer] == val and nums[rightPointer] == val:
                rightPointer -= 1
            elif nums[leftPointer] == val and nums[rightPointer] != val:
                nums[leftPointer], nums[rightPointer] = nums[rightPointer], nums[leftPointer]
                leftPointer += 1
                rightPointer -= 1
            elif nums[leftPointer] != val:
                leftPointer += 1
            else:
                leftPointer += 1

        idxCount = 0
        for i in range(len(nums)):
            if nums[i] == val:
                idxCount += 1
        
        nums = nums[:len(nums)-idxCount]
        return len(nums)


        

