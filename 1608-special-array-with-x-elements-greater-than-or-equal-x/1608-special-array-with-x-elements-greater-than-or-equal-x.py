from collections import defaultdict
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        bins = defaultdict(int)
        for num in nums:
            bins[min(n, num)] += 1
        
        val = 0
        for i in range(n, 0, -1):
            val += bins[i]
            
            if val == i:
                return i
        
        return -1
        
        
        
            