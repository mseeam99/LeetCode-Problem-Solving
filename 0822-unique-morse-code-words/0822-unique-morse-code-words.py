class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:

        morse_Code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        morse_Code_hashMap = {}

        for i in range(len(morse_Code)):
            morse_Code_hashMap[chr(64+i+1)] = morse_Code[i]

        mySet = set()

        for i in range(len(words)):
            tempString = ""
            for j in range(len(words[i])):
                tempString += morse_Code_hashMap[(words[i][j]).upper()]
                        
            mySet.add(tempString)

        return len(mySet)




    