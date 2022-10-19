class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        d = {}
        
        for idx, value in enumerate(nums):
            if target - value in d: 
                return [idx, d[target - value]]
            d[value] = idx
            
        