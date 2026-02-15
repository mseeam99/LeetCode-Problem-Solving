class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:

        if (len(sentence1) != len(sentence2)):
            return False
        
        if len(similarPairs) == 0:
            if sentence1 == sentence2:
                return True

        count = 0
        for i in range(len(sentence1)):
            if sentence1[i] == sentence2[i]:
                count += 1
                continue

            for j in range(len(similarPairs)):
                if (similarPairs[j][0] == sentence1[i]) and (similarPairs[j][1] == sentence2[i]) or (similarPairs[j][1] == sentence1[i]) and (similarPairs[j][0] == sentence2[i]) :
                    count += 1
                    break

        return True if count == len(sentence1) else False
        