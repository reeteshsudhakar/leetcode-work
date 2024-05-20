class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def dfs(idx: int, curr_xor: int) -> int:
            if idx == len(nums): return curr_xor
            
            exclude = dfs(idx + 1, curr_xor)
            include = dfs(idx + 1, curr_xor ^ nums[idx])
            
            return include + exclude
        
        return dfs(0, 0)
            