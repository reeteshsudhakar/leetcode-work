class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:     
        def dfs(target, candidates, path):
            if target == 0:
                ret.append(path.copy())
                return
            elif target < 0:
                return
            
            for i in range(len(candidates)):
                if i > 0 and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                
                dfs(target - candidates[i], candidates[i + 1:], path + [candidates[i]])
        
        ret = []
        candidates.sort()
        dfs(target, candidates, [])
        return ret