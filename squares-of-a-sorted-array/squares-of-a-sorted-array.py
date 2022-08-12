class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        start = 0
        end = len(nums) - 1
        
        result = []
        
        while (start <= end):
            if (nums[start]**2 > nums[end]**2):
                result.append(nums[start]**2)
                start += 1
            else:
                result.append(nums[end]**2)
                end -= 1
        
        return result[::-1]