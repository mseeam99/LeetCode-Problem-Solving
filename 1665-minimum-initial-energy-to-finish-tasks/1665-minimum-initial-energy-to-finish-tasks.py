class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x : x[1]-x[0])
        answer = 0
        for i in range(len(tasks)):
            answer = max(answer + tasks[i][0], tasks[i][1])
        return answer