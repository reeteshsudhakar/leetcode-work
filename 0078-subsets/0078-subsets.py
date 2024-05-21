class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        
        def dfs(idx: int, curr_arr: List[int]):
            if idx == len(nums): 
                if curr_arr not in ret: ret.append(curr_arr)
                return
            
            dfs(idx + 1, curr_arr)
            dfs(idx + 1, curr_arr + [nums[idx]])
        
        dfs(0, [])
        return list(ret)