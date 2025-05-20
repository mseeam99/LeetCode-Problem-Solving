class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        array = [-1] * (target+1)
        
        def recursion(n):

            if n > target:
                return 0
            if n == target:
                return 1
            if array[n] != -1:
                return array[n]

            res = 0

            for num in nums:
                res += recursion(n + num)
            
            array[n] = res
            return res

        return recursion(0)

