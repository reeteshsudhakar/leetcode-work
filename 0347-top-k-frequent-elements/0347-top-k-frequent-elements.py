from collections import defaultdict

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        d = defaultdict(int)
        
        for i in nums: 
            d[i] += 1
        
        return sorted(d, key = d.get, reverse = True)[:k]
                