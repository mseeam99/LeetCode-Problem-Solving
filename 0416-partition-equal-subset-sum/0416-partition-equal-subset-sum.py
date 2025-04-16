class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)

        if total % 2 != 0:
            return False

        half = total // 2

        print("TOTAL: ", total)
        print("HALF : ", half)

        dp = set()
        dp.add(0)

        for i in range(len(nums)-1,-1,-1):
            print(dp)
            dpTempArray = set()
            for val in dp:
                if nums[i] + val == half:
                    return True
                dpTempArray.add(val)
                dpTempArray.add(nums[i]+val)
            dp = dpTempArray
            
        print(dp)
        return True if half in dp else False

        



        