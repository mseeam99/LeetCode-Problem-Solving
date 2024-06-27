class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        answer = 0
        i = 0
        while i < len(colors):
            current_char = colors[i]
            total_time = 0
            max_time = 0
            while i < len(colors) and colors[i] == current_char:
                total_time += neededTime[i]
                max_time = max(max_time, neededTime[i])
                i += 1
            answer += total_time - max_time
        return answer







