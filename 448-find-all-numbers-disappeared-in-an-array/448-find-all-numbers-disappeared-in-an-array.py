class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        result = []
        for num in nums: 
            curr = abs(num)
            if nums[curr - 1] < 0:
                continue
            nums[curr - 1] = -nums[curr - 1]
        
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
        
        return result