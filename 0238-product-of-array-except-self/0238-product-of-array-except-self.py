class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        
        product = 1
        
        for i in nums: 
            ret.append(product)
            product *= i 
        
        # at this point, ret will be [1, a, ab, abc]
        
        product = 1
        
        for i in reversed(range(len(nums))):
            ret[i] *= product
            product *= nums[i]
    
        # at this point, ret will be [1 * bcd, a * cd, ab * d, abc * 1]
        return ret