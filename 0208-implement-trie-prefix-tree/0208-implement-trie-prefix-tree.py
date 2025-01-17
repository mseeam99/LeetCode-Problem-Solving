class TrieNode():
    def __init__(self):
        self.hashMap = {}
        self.isEnd   = False

class Trie:
    def __init__(self):
        self.thePrefixTree = TrieNode()
        
    def insert(self, word: str) -> None:
        theCopy = self.thePrefixTree
        for i in range(len(word)):
            if word[i] not in theCopy.hashMap:
                theCopy.hashMap[word[i]] = TrieNode()
            theCopy = theCopy.hashMap[word[i]]
        theCopy.isEnd = True
        
    def search(self, word: str) -> bool:
        theCopy = self.thePrefixTree
        for i in range(len(word)):
            if word[i] not in theCopy.hashMap:
                return False
            theCopy = theCopy.hashMap[word[i]]
        return theCopy.isEnd
        
    def startsWith(self, prefix: str) -> bool:
        theCopy = self.thePrefixTree
        for i in range(len(prefix)):
            if prefix[i] not in theCopy.hashMap:
                return False
            else:
                if i == len(prefix)-1 and theCopy.isEnd == False:
                    return True
            theCopy = theCopy.hashMap[prefix[i]]
        return True

       




# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)