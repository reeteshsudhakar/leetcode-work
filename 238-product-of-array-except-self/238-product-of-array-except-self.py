class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        length = len(nums)
        product = 1
        zeroesCount = 0
        
        for i in nums:
            if i == 0:
                zeroesCount += 1
            else:
                product *= i
                
        if zeroesCount > 1:
            return [0] * length
        elif zeroesCount == 1:
            for i in range(length):
                if nums[i] != 0:
                    nums[i] = 0;
                else:
                    nums[i] = product
        else: 
            for i in range(length):
                nums[i] = product // nums[i]
        
        return nums