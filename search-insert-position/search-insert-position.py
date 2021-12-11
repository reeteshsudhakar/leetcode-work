class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums: 
            return nums.index(target)
        else: 
            for i in range(len(nums) - 1): 
                if target > nums[i] and target < nums[i + 1]:
                    return i + 1
            if target > nums[len(nums) - 1]: 
                return len(nums)
            elif target < nums[0]:
                return 0
                    