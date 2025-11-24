# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        answer = ListNode(head.val,None)
        answerHead = answer
        lastValue = -101

        while head:
            currentValue = head.val
            while head and head.val == currentValue:
                head = head.next
            
            if head:
                answer.next = ListNode(head.val,None)
                answer = answer.next

        
        return answerHead







        
       
            
 
        