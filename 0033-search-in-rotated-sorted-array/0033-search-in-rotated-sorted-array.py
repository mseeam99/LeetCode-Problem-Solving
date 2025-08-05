class Solution:
    def search(self, nums: List[int], target: int) -> int:

        answer = -1
        leftPointer = 0
        rightPointer = len(nums)-1

        while leftPointer <= rightPointer:

            middlePointer = int(leftPointer + (rightPointer - leftPointer) // 2)

            if nums[middlePointer] == target:
                return middlePointer

            if nums[leftPointer] <= nums[middlePointer]:
                if nums[leftPointer] <= target < nums[middlePointer]:
                    rightPointer = middlePointer - 1
                else:
                    leftPointer = middlePointer + 1
            else:
                if nums[middlePointer] < target <= nums[rightPointer]:       
                    leftPointer = middlePointer + 1
                else:
                    rightPointer = middlePointer - 1

        return answer


