import sys
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        minimum = sys.maxsize
        
        for i in range(len(nums) - 2):
            low = i + 1
            high = len(nums) - 1
            
            while low < high:
                diff = nums[i] + nums[low] + nums[high] - target
                if abs(diff) < abs(minimum):
                    minimum = diff
                
                if diff == 0:
                    return target
                elif diff < 0:
                    low += 1
                else: 
                    high -= 1
            
        
        return minimum + target