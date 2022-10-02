class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        
        def dfs(target, path, k):
            if target < 0:
                return
            elif target == 0:
                ret.append(path)
                return
            else:
                for i in range(k, len(candidates)):
                    dfs(target - candidates[i], path + [candidates[i]], i)
        
        dfs(target, [], 0)
        return ret