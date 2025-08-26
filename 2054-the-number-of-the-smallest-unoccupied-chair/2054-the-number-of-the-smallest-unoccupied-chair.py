class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:

        for i in range(len(times)):
            times[i].append(i)

        times.sort(key=lambda x: (x[0], x[2]))

        available = []
        for i in range(len(times)):
            available.append(i)
        heapq.heapify(available)

        using = []

        for arrive, leave, friend in times:
            while using and using[0][0] <= arrive:
                _, chair = heapq.heappop(using)
                heapq.heappush(available, chair)

            chair = heapq.heappop(available)
            heapq.heappush(using, (leave, chair))

            if friend == targetFriend:
                return chair
