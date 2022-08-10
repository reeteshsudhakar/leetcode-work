class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        left = 0
        right = sum(nums)
        
        for idx, num in enumerate(nums):
            right -= num
            if left == right:
                return idx
            else:
                left += num
        
        return -1