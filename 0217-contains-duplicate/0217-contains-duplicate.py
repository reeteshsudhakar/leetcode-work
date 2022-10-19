from collections import defaultdict
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        d = defaultdict(int)
        
        for i in nums: 
            if i in d: 
                return True
            d[i] = 1
        return False