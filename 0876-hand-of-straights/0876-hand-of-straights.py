class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hashMap = {}
        for i in range(len(hand)):
            if hand[i] not in hashMap:
                hashMap[hand[i]]=1
            elif hand[i] in hashMap:
                hashMap[hand[i]]+=1
        minHeap = list(hashMap.keys())
        heapq.heapify(minHeap)
        while minHeap:
            first = minHeap[0]
            for i in range(first,first+groupSize):
                if i not in hashMap:
                    return False
                hashMap[i]-=1
                if hashMap[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True
        