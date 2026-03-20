class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]: 
        tickets.sort(reverse=True)
        graph = defaultdict(list)
        for start, end in tickets:
            graph[start].append(end)
        result = []
        def dfs(src):
            while graph[src]:
                next_dst = graph[src].pop()
                dfs(next_dst)
            result.append(src)
        dfs("JFK")
        return result[::-1]
        