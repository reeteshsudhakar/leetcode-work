class Solution(object):
    def removeDuplicates(self, nums):
        idx = 1
        underscore_count = 0
        
        for i in range(len(nums) - 1):
            if nums[i] != nums[i+1]:
                nums[idx] = nums[i+1]
                idx += 1
            else: 
                underscore_count += 1
        return idx
                
        