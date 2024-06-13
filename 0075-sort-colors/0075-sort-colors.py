from collections import Counter
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        counter = Counter(nums)
        
        i = 0
        while i < len(nums):
            for (num, count) in sorted(counter.items(), key=lambda x: x[0]):
                for j in range(count):
                    nums[i + j] = num
                i += count
        