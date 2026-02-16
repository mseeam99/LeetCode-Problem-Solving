class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        
        memo = {}

        def recursion(index: int, previousIndex: int) -> List[str]:
            if index >= len(words):
                return []

            key = (index, previousIndex)
            if key in memo:
                return memo[key]

            best = recursion(index + 1, previousIndex)

            if previousIndex == -1 or groups[index] != groups[previousIndex]:
                best = [words[index]] + recursion(index + 1, index)
                

            memo[key] = best
            return best

        return recursion(0, -1)
