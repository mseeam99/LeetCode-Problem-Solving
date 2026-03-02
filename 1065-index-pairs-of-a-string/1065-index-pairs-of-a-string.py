class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        mySet = set(words)
        answer = []
        for i in range(len(text)):
            currentString = ""
            for j in range(i,len(text)):
                currentString += text[j]
                if currentString in mySet:
                    answer.append([i,j])
        return answer


                
        