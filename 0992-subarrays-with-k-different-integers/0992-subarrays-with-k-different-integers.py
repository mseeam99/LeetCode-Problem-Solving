class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def helper(val):
            
            hashMap = {}

            leftPointer = 0
            rightPointer = 0
            subArray = 0

            while rightPointer <= len(nums)-1:

                if nums[rightPointer] not in hashMap:
                    hashMap[nums[rightPointer]] = 1
                else:
                    hashMap[nums[rightPointer]] += 1

                while len(hashMap) > val:
                    hashMap[nums[leftPointer]] -= 1
                    if hashMap[nums[leftPointer]] == 0:
                        del hashMap[nums[leftPointer]]
                    leftPointer += 1

                subArray += (rightPointer-leftPointer)+1
                rightPointer += 1

            return subArray


        return helper(k)-helper(k-1)



                





        