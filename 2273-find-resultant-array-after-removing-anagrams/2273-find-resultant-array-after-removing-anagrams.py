class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        answer = []
        answer.append(words[0])
        for i in range(1,len(words)):
            if Counter(answer[-1]) == Counter(words[i]):
                pass
            else:
                answer.append(words[i])
        return answer




        