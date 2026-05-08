class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:


        hashMap = defaultdict(list)
        returnStatement = False

        for i in range(len(nums)):

            if nums[i] not in hashMap:
                hashMap[nums[i]].append(i)

            elif nums[i] in hashMap:
                hashMap[nums[i]].append(i)

                theList = hashMap[nums[i]]
                for j in range(len(theList)):

                
                    if (abs(theList[j]-i) <= k) and (theList[j]!=i):
                        returnStatement = True
                        return True


        return returnStatement



       




        



