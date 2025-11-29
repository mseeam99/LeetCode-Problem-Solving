# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        mySet = set(nums)
        pointerOne = head
        currentPointer = head
        newHead = None

        while pointerOne != None:
            while pointerOne and pointerOne.val in mySet:
                pointerOne = pointerOne.next
            if pointerOne:
                if newHead == None:
                    newHead = pointerOne
                    currentPointer = pointerOne
                else:
                    currentPointer.next = pointerOne
                    currentPointer = currentPointer.next
                pointerOne = pointerOne.next

            
        if currentPointer:
            currentPointer.next = None
        return newHead
            