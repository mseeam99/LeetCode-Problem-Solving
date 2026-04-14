class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        hashMap = {}
        for i in range(len(nums)):
            hashMap[nums[i]] = i   # store last index of each value

        answers = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                currentSum = nums[i] + nums[j]
                diffNeed = -currentSum

                if diffNeed in hashMap and hashMap[diffNeed] > j:
                    answers.append([nums[i], nums[j], diffNeed])

        return answers