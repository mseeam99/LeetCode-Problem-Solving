# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        headPointer = head
        values = []
        index = 0
        while headPointer != None:
            if index % 2 == 0:
                values.append(headPointer.val)
            headPointer = headPointer.next
            index+=1
        headPointer = head
        index = 0
        while headPointer != None:
            if index % 2 != 0:
                values.append(headPointer.val)
            headPointer = headPointer.next
            index+=1
        headPointer = head
        index = 0
        while headPointer != None:
            headPointer.val = values[index]
            index+=1
            headPointer = headPointer.next
        return head

        

        


        
        