class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:

        hashMap = set(friends)
        
        answer = []
        for i in range(len(order)):
            if order[i] in hashMap:
                answer.append(order[i])
        return answer

        