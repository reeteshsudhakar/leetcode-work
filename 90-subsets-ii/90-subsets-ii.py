class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = []
        
        nums.sort()
        
        def dfs(nums, path):
            ret.append(path)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                dfs(nums[i + 1:], path + [nums[i]])
        
        dfs(nums, [])
        return ret