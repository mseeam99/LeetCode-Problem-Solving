class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        hashMap = {
            'b': 0,
            'a': 0,
            'l': 0,
            'o': 0,
            'n': 0
        }
        for char in text:
            if char in hashMap:
                hashMap[char] += 1

        hashMap['l'] //= 2  
        hashMap['o'] //= 2  

        return min(hashMap.values())



        