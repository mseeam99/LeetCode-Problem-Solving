class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:

        def checkIfPrefix(string,word):
            for i in range(len(word)):
                if word[i] != string[i]:
                    return False
            return True

        array = sentence.split(" ")
        for i in range(len(array)):
            if searchWord in array[i]:
                if checkIfPrefix(array[i],searchWord) == True:
                    return i+1
            
        return -1

        