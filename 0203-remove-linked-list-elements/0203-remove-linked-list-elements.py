class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        dummy = ListNode(0,None)
        dummy.next = head
        current = dummy

        while current.next != None:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next