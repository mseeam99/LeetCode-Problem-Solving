class Solution:
    def partition(self, s: str) -> List[List[str]]:

        biggerArray = []
        innerArray = []

        def recursion(start):

            if start >= len(s):
                biggerArray.append(innerArray.copy())
                return
            
            for end in range(start,len(s)):

                subString = s[start:end+1]
                

                if subString == subString[::-1]:
                    innerArray.append(subString)
                    recursion(end+1)
                    innerArray.pop()




        recursion(0)
        return biggerArray


        