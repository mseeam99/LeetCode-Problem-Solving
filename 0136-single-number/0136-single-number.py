class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        hashMap = Counter(nums)
        for k,v in hashMap.items():
            if v == 1:
                return k