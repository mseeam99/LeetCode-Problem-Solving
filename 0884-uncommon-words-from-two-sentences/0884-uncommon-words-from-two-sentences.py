class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:

        if len(s1) < len(s2):
            s1,s2 = s2,s1
        
        s1 = s1.split(" ")
        s2 = s2.split(" ")
        
        hashMapOne = {}
        hashMapTwo = {}

        for i in range(len(s1)):
            if s1[i] not in hashMapOne:
                hashMapOne[s1[i]] = 1
            else:
                hashMapOne[s1[i]] += 1
        
        for i in range(len(s2)):
            if s2[i] not in hashMapTwo:
                hashMapTwo[s2[i]] = 1
            else:
                hashMapTwo[s2[i]] += 1

        answer = []
        for key,val in hashMapOne.items():
            if hashMapOne[key] == 1 and key not in hashMapTwo:
                answer.append(key)
        
        for key,val in hashMapTwo.items():
            if hashMapTwo[key] == 1 and key not in hashMapOne:
                answer.append(key)



        return answer
        

        