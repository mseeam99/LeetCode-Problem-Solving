class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_dict = {}

        for num in nums:
            if num not in freq_dict:
                freq_dict[num] = 1
            else:
                freq_dict[num] += 1

        sorted_dict = sorted(freq_dict, key = freq_dict.get, reverse = True)
        return sorted_dict[:k]
        

        
       

        
        