class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        answer = []

        leftPointer = 0
        rightPointer = len(nums)-1

        while len(answer) != len(nums):
            answer.append(nums[leftPointer])
            leftPointer+=1

            if leftPointer < rightPointer:
                answer.append(nums[rightPointer])
                rightPointer-=1

        return answer

        
        

        