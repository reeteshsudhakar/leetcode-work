class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        counter = 0
        idx = 0
        
        while idx < len(nums):
            if nums[idx] == 0:
                counter += 1
                nums.pop(idx)
            else:
                idx += 1
                
        for i in range(counter):
            nums.append(0)
        