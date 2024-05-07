class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # Do not know why not working
        '''
        firstPart = nums[0:k]
        secondPart = nums[k:]
        print("first: " , firstPart)
        print("second:" , secondPart)
        nums.clear()
        nums[:] = secondPart + firstPart
        return nums
        '''
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        return nums