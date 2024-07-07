class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        
        def dfs(i: int, candidate: List[int], total: int) -> None:
            if total == target:
                ret.append(candidate[:])
                return
            
            if total > target or i >= len(candidates):
                return
            
            candidate.append(candidates[i])
            dfs(i, candidate, total + candidates[i])
            candidate.pop()
            dfs(i + 1, candidate, total)
        
        dfs(0, [], 0)
        return ret