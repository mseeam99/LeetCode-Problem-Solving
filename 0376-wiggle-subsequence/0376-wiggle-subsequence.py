class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:

        memo = {}
        
        def recursion(index,prevIndex,increasing):

            if (index >= len(nums)) or (prevIndex >= len(nums)):
                return 0
            
            if (index,prevIndex,increasing) in memo:
                return memo[(index,prevIndex,increasing)]

           
            best = recursion(index + 1, prevIndex, increasing)

            if prevIndex == -1:
                best = max(best,1+recursion(index + 1, index, increasing))
            else:
                if increasing == True:
                    if nums[index] > nums[prevIndex]:
                        best = max(best, 1 + recursion(index + 1, index, False))
                else:
                    if nums[index] < nums[prevIndex]:
                        best = max(best, 1 + recursion(index + 1, index, True))

            memo[(index,prevIndex,increasing)] = best
            return memo[(index,prevIndex,increasing)]

      
        return max(recursion(0, -1, True), recursion(0, -1, False))



        
        