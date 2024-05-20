class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr = arr[::-1]
        res = []
        max_so_far = -1
        for i in arr:
            res.append(max_so_far)
            if i>max_so_far:
                max_so_far = i


        return res[::-1]