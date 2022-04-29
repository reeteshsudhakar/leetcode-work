class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = {}
        
        for i in range(len(nums)):
            if target - nums[i] in result:
                return [i, result[target - nums[i]]]
            
            result[nums[i]] = i