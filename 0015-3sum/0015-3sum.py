class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            leftPointer = i+1
            rightPointer = len(nums)-1
            while leftPointer < rightPointer:
                if nums[i] + nums[leftPointer] + nums[rightPointer] == 0:
                    answer.add((nums[i],nums[leftPointer],nums[rightPointer]))
                    leftPointer+=1
                    rightPointer-=1
                elif nums[i] + nums[leftPointer] + nums[rightPointer] < 0:
                    leftPointer += 1
                elif nums[i] + nums[leftPointer] + nums[rightPointer] > 0:
                    rightPointer -= 1
        answer = list(answer)
        return answer
                
        