class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int: 

        total = sum(stones)  
        target = sum(stones) // 2
        answer = float("inf")
        memo = {}

        def recursion(current,index):
            nonlocal answer

            if (index,current) in memo:
                return (index,current)
                
            if index == len(stones):
                need = total - current
                answer = min(answer,abs(current-need))
                return answer

            memo[(index,current)] = recursion(current+stones[index],index+1)
            memo[(index,current)] = recursion(current,index+1)

        recursion(0,0)
        return answer
        
        