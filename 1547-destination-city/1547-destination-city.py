class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        firstPair = set()
        for i in range(len(paths)):
            firstPair.add(paths[i][0])

        secondPair = set()
        for i in range(len(paths)):
            secondPair.add(paths[i][1])

        answer = secondPair - firstPair
        return list(answer)[0]

        
        

        