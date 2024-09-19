class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks = Counter(tasks)
        task_values = [-i for i in tasks.values()]
        myDeque = deque()
        heapq.heapify(task_values)
        time = 0
        while len(task_values) != 0 or len(myDeque) != 0:
            time+=1
            if len(task_values)!=0:
                max_value = heapq.heappop(task_values) + 1
                if max_value:
                    myDeque.append([max_value,time+n])
            if len(myDeque) != 0 and myDeque[0][1] == time:
                heapq.heappush(task_values,myDeque.popleft()[0])
        return time

        