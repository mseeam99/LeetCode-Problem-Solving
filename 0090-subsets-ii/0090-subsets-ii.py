class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        mySet = set([])
        mySet.add(tuple([]))
        def recursion(index,nums,changingList):
            if index == len(nums):
                mySet.add(tuple(changingList))
                return
            recursion(index+1,nums,changingList+[nums[index]])
            recursion(index+1,nums,changingList)
            return
        recursion(0,nums,[])
        return list(mySet)

            
