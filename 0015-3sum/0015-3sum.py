class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        nums.sort()
        print(nums)
        ret = []
        
        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i - 1]: continue
            
            j = i + 1
            k = n - 1
            
            while j < k:
                val = nums[i] + nums[j] + nums[k]
                if val == 0:
                    l = [nums[i], nums[j], nums[k]]
                    if l not in ret: ret.append(l)
                    j += 1
                    k -= 1
                
                elif val < 0:
                    j += 1
                
                elif val > 0:
                    k -= 1
        
        return ret