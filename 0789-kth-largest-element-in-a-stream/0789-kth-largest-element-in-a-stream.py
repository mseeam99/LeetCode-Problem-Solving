class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.myArray = nums
        self.myK = k
        heapq.heapify(self.myArray)
        while len(self.myArray)>k:
            heapq.heappop(self.myArray)

    def add(self, val: int) -> int:
        heapq.heappush(self.myArray,val)
        if len(self.myArray) > self.myK:
            heapq.heappop(self.myArray)
        return self.myArray[0]