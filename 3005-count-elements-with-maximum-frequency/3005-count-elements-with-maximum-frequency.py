from collections import Counter

class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        counter = Counter(nums)        
        l = [num for num in counter.values()]
        
        return max(l) * l.count(max(l))