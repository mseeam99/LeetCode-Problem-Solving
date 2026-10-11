class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = 1
            else:
                hashMap[nums[i]] += 1
        array = []
        for key,val in hashMap.items():
            array.append((val,key))
        heapq.heapify(array)
        array = heapq.nlargest(k,array)
        returnArray = []
        for i in range(k):
            returnArray.append(array[i][1])
        return returnArray 
        '''
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = 1
            else:
                hashMap[nums[i]] += 1
        
        print(hashMap)
        array = []
        for i in range(len(nums)+1):
            array.append([])
        

        for key,val in hashMap.items():
            array[val].append(key)
        
        answer = []
        count = 0
        for i in range(len(array)-1,-1,-1):
            if len(array[i])!=0:
                for j in range(len(array[i])):
                    if count >= k:
                        break
                    answer.append(array[i][j])
                    count += 1


        return answer











        

        
       

        
        