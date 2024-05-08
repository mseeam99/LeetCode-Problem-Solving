class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        answer = set()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            leftPointer = i+1
            rightPointer = leftPointer+1
            while leftPointer < len(nums)-1:
                value = nums[i] + nums[leftPointer] + nums[rightPointer]
                if value == 0:
                    answer.add(tuple(sorted([nums[i],nums[leftPointer], nums[rightPointer]])))
                    if rightPointer != len(nums)-1:
                        rightPointer+=1
                    elif rightPointer == len(nums)-1:
                        leftPointer +=1
                        rightPointer = leftPointer+1
                else:
                    if rightPointer != len(nums)-1:
                        rightPointer+=1
                    elif rightPointer == len(nums)-1:
                        leftPointer +=1
                        rightPointer = leftPointer+1
        answer = list(answer)
        return answer
        '''
        
        nums.sort()
        answer = set()
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
                    leftPointer+=1
                elif nums[i] + nums[leftPointer] + nums[rightPointer] > 0:
                    rightPointer-=1
        answer = list(answer)
        return answer