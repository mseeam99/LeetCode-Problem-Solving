class Solution(object):
    def lastSubstring(self, s):
        prev = ptr = cur = 0
        for i, c in enumerate(s[1:], 1):
            ptr += 1
            if c > s[prev]:     prev = ptr = cur = i
            elif c == s[prev]:
                if c > s[ptr]:  prev, ptr, cur = cur, cur, i
                elif c>s[i-1]:  ptr, cur = prev, i
            elif c > s[ptr]:    prev, ptr = cur, i
            elif c < s[ptr]:    ptr, cur = i, prev
        return s[prev:]