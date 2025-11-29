# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        mySet = set(nums)
        pointerOne = head
        myNewlist = ListNode()
        headTrack = myNewlist
        while pointerOne != None:
            if pointerOne and pointerOne.val in mySet:
                pointerOne = pointerOne.next
            else:
                newNode = ListNode(pointerOne.val)
                myNewlist.next = newNode
                myNewlist = myNewlist.next
                pointerOne = pointerOne.next
        return headTrack.next


