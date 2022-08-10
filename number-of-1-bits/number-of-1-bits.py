class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bin_string = str(bin(n))
        
        count = 0
        for char in bin_string:
            if char == "1":
                count += 1
        
        return count