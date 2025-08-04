class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def subsetFunction(arr,sum):
            previousDp = [False] * (sum+1)
            previousDp[0] = True
            for row in range(len(arr)):
                currentDp = [False] * (sum+1)
                currentDp[0] = True
                for col in range(1,sum+1):
                    notTake = previousDp[col]
                    take = False
                    if arr[row] <= col:
                        take = previousDp[col-arr[row]]
                    currentDp[col] = take or notTake
                previousDp = currentDp
            return previousDp[sum]
        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2
        return subsetFunction(nums,target)


