class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        
        curr_sum = 0
        count = {0 : 1}
        ret = 0 
        
        for num in nums: 
            curr_sum += num
            
            if curr_sum - goal in count:
                ret += count[curr_sum - goal]
                
            count[curr_sum] = count.get(curr_sum, 0) + 1
        
        return ret