class Solution:
    def isPalindrome(self, x: int) -> bool:

        new = str(x)
        newReversed = new[::-1]

        if new == newReversed:
            return True
        else:
            return False
        