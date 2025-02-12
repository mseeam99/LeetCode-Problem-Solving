class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        array = [0] * (n + 1)  
        
        for i in range(len(trust)):
            temp = trust[i][1]  
            array[temp] += 1  
            array[trust[i][0]] -= 1  

        print(array) 

        for i in range(1, n + 1):  
            if array[i] == n - 1:  
                return i
        
        return -1 
