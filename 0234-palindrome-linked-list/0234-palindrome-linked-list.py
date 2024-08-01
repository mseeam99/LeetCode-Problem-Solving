class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        myList = []
        tempHead = head

        while head != None:
            myList.append(head.val)

        return myList == myList[::-1]
        