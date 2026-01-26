class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        mySet = set()
        for i in range(len(nums)):
            mySet.add(nums[i] * - 1)
        mySet = list(mySet)

        heapq.heapify(mySet)
        answer = 0
        if len(mySet) >= 3:
            for i in range(3):
                answer = heapq.heappop(mySet) * (-1)
        else:
            return min(mySet) * -1
        return answer

        