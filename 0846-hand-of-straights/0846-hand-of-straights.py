class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        hashMap = Counter(hand)
        hand = list(hashMap.keys())
        
        heapq.heapify(hand)

        visitedSet = set()

        duplicateStore = []

        lastPopped = hand[0]-1

        while hand:

            poppedVal = heapq.heappop(hand)

            hashMap[poppedVal] -= 1
            if hashMap[poppedVal] == 0:
                del hashMap[poppedVal]
            elif hashMap[poppedVal] > 0:
                duplicateStore.append(poppedVal)
                
            if lastPopped is None or poppedVal == lastPopped + 1:
                visitedSet.add(poppedVal)
                lastPopped = poppedVal
            else:
                return False
                    
            
            if len(visitedSet) == groupSize:
                print("visited   set: ",visitedSet)
                print("duplicate lst: ",duplicateStore)
                for i in range(len(duplicateStore)):
                    heapq.heappush(hand,duplicateStore[i])
                duplicateStore.clear()
                visitedSet.clear()
                lastPopped = None


        print(duplicateStore)
        if len(duplicateStore) == 0:
            return True
        else:
            return False
















        
    
        
        