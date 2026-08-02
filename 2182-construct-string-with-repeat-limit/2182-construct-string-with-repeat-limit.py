class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        hashMap = Counter(s)
        maxHeap = []
        for char,count in hashMap.items():
            maxHeap.append((-ord(char),count))
        heapq.heapify(maxHeap)
        result = []
        while maxHeap:
            char, count = heapq.heappop(maxHeap)
            char = char*-1
            char = chr(char)
            nextIteration = min(count,repeatLimit)
            result.append(char*nextIteration)
            if count-nextIteration > 0 and maxHeap:
                secondChar, secondCount = heapq.heappop(maxHeap)
                secondChar = secondChar*-1
                secondChar = chr(secondChar)
                result.append(secondChar)
                if secondCount-1 > 0:
                    heapq.heappush(maxHeap,(-ord(secondChar),abs(secondCount-1)))
                heapq.heappush(maxHeap,(-ord(char),abs(count-nextIteration)))
        return "".join(result)