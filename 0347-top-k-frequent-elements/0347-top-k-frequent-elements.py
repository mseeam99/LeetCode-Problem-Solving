class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        freq_dict = {}
        for num in nums:
            if num not in freq_dict:
                freq_dict[num] = 1
            else:
                freq_dict[num] += 1
        sorted_dict = sorted(freq_dict, key = freq_dict.get, reverse = True)
        return sorted_dict[:k]
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








        

        
       

        
        