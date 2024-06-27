class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        answer  = 0
        pointer = 0

        while pointer < len(colors):
            tempColor  = colors[pointer]
            max_time   = 0
            total_time = 0
            while pointer < len(colors) and colors[pointer] == tempColor:
                total_time += neededTime[pointer]
                max_time = max(max_time,neededTime[pointer])
                pointer+=1
            answer += (total_time-max_time)
        return answer

        

        