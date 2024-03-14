class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ret = 0
        num_set = set(nums)
        
        for num in num_set:
            if (num - 1) not in num_set:
                length = 1
                while (num + length) in num_set:
                    length += 1
                
                ret = max(length, ret)
        
        return ret