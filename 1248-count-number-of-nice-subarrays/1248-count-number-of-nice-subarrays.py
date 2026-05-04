class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def helper(val):
            leftPointer = 0
            rightPointer = 0
            oddCount = 0
            subarrayCount = 0
            while rightPointer <= len(nums)-1:
                if nums[rightPointer] % 2 != 0:
                    oddCount += 1
                while oddCount > val:
                    if nums[leftPointer] % 2 != 0:
                        oddCount -= 1
                    leftPointer += 1
                subarrayCount += ((rightPointer-leftPointer)+1)
                rightPointer += 1
            return subarrayCount
        return helper(k) - helper(k-1)