# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        answerArray = []
        firstArray = []
        secondArray = []
        headOne = l1
        headTwo = l2
        while headOne != None:
            firstArray.append(headOne.val)
            headOne = headOne.next
        while headTwo != None:
            secondArray.append(headTwo.val)
            headTwo = headTwo.next
        firstArrayIndex = len(firstArray)-1
        secondArrayIndex = len(secondArray)-1
        current = 0
        while firstArrayIndex >= 0 or secondArrayIndex >= 0:
            if firstArrayIndex >= 0:
                valueOne = firstArray[firstArrayIndex]
            else:
                valueOne = 0
            if secondArrayIndex >= 0:
                valueTwo = secondArray[secondArrayIndex]
            else:
                valueTwo = 0
            addition = valueOne + valueTwo + current
            answerArray.append(addition%10)
            current = addition // 10
            firstArrayIndex-=1
            secondArrayIndex-=1
        if current != 0:
            answerArray.append(current)
        answerArray = answerArray[::-1]

        
        newList = ListNode()
        answer = newList
        for i in range(len(answerArray)):
            newList.val = answerArray[i]
            if i != len(answerArray)-1:
                newList.next = ListNode()
                newList = newList.next
       
            


        return answer

        





            



        
        
        