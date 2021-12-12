class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        solution = {}
        
        for i in nums:
            if i in solution:
                solution[i] += 1
            else:
                solution[i] = 1
        
        for key, value in solution.items():
            if value == 1:
                return key 