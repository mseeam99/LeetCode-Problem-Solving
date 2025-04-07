class Solution:
    def countSubstrings(self, s: str) -> int:

        count = 0

        def expandODD(i):
            nonlocal s
            nonlocal count
            left  = i
            right = i
            while True:
                if left >= 0 and right <= len(s)-1:
                    if s[left] == s[right]:
                        count+=1
                        left-=1
                        right+=1
                    else:
                        break
                else:
                    break

        def expandEVEN(i):
            nonlocal s
            nonlocal count
            left  = i
            right = i+1
            while True:
                if left >= 0 and right <= len(s)-1:
                    if s[left] == s[right]:
                        count+=1
                        left-=1
                        right+=1
                    else:
                        break
                else:
                    break


    
        for i in range(len(s)):
            expandODD(i)
            expandEVEN(i)

        print(count)

        return count




        