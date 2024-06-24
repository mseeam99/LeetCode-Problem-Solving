class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        mySet = set()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                leftPointer  = j + 1
                rightPointer = len(nums) - 1
                while leftPointer < rightPointer:
                    value = nums[i]+nums[j]+nums[leftPointer]+nums[rightPointer]
                    if value == target:
                        tempList = (nums[i],nums[j],nums[leftPointer],nums[rightPointer])
                        mySet.add((tempList))
                        leftPointer+=1
                        rightPointer-=1
                    elif value < target:
                        leftPointer+=1
                    elif value > target:
                        rightPointer-=1
        sorted(mySet)
        return list(mySet)

        

        