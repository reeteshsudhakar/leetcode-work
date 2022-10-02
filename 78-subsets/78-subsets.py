class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        
        def dfs(nums, path):
            ret.append(path)
            for i in range(len(nums)):
                dfs(nums[i + 1:], path + [nums[i]])
        
        dfs(nums, [])
        return ret