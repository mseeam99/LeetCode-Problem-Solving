class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        myQueue = [0]
        mySet = set()
        farthest = 0
        while myQueue:
            pointer = myQueue.pop(0)
            left  = max(pointer+minJump,farthest+1)
            right = min(pointer+maxJump+1,len(s))
            for i in range(left,right):
                if s[i] == "0" and i not in mySet:
                    if i == len(s)-1:
                        return True
                    myQueue.append(i)
                    mySet.add(i)
            farthest = max(farthest, pointer + maxJump)
        return True if len(s) - 1 in mySet else False
        