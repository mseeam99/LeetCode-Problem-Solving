class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        print(xor)
        for i in range(len(nums)):
            xor = xor ^ nums[i]
            print(xor)
        return xor
        