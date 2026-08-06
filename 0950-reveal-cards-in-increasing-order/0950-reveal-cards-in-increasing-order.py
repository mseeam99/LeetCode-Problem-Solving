class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        returnArray = [0] * len(deck)
        q = deque(range(len(deck)))
        for i in range(len(deck)):
            indexICanUse = q.popleft()
            if q:
                q.append(q.popleft())
            returnArray[indexICanUse] = deck[i]
        return returnArray

            

        