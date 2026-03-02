class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:

        hashMap = {}
        for i in range(1,27):
            hashMap[chr(64+i).lower()] = weights[i-1]

        output = []

        for i in range(len(words)):
            currentWeightedSum = 0
            for j in range(len(words[i])):
                currentWeightedSum += hashMap[words[i][j]]
            currentWeightedSum = currentWeightedSum % 26
            output.append(currentWeightedSum)

        hashMap.clear()

        for i in range(26):
            hashMap[i] = chr(90-i).lower()
        
        for i in range(len(output)):
            output[i] = hashMap[output[i]]

        return "".join(output)
            

        



        

        