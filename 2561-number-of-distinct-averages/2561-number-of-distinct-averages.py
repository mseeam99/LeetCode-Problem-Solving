class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        mySet = set()
        left = 0
        right = len(nums)-1
        count = 1
        while left <= right:
            avgValue = (nums[left] + nums[right]) / 2
            mySet.add(avgValue)
            left+=1
            right-=1
        return len(mySet)


            
