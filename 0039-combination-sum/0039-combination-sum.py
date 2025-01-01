class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        answer = []
        subset = []

        def dfs(index):

            if sum(subset) > target or index >= len(candidates):
                return
           
            if sum(subset) == target:
                answer.append(subset.copy())
                return

            #CHOOSE 
            subset.append(candidates[index])
            dfs(index)

            #MIDDLE

            #NOT CHOOSE
            subset.pop()
            dfs(index+1)
            
        dfs(0)
        return answer
        