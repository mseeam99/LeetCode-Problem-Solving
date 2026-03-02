class TrieNode:
    def __init__(self):
        self.hashMap = {}
        self.isWord = False

class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        root = TrieNode()
        for i in range(len(words)):
            node = root 
            for j in range(len(words[i])):
                if words[i][j] not in node.hashMap:
                    node.hashMap[words[i][j]] = TrieNode()
                node = node.hashMap[words[i][j]]
            node.isWord = True

        answer = []
        for i in range(len(text)):
            node = root            
            for j in range(i, len(text)):
                char = text[j]    
                if char not in node.hashMap:
                    break   
                node = node.hashMap[char]
                if node.isWord:
                    answer.append([i, j])
        
        return answer
                


        

        



        

                
        