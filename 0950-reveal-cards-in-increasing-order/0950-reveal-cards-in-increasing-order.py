class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:

        deck.sort()
        returnArray = [0] * len(deck)
        q = deque(range(len(deck)))


        for i in range(len(deck)):

            value = deck[i]

            index = q.popleft()


            returnArray[index] = value

            if q:
                q.append(q.popleft())






        return returnArray





        
