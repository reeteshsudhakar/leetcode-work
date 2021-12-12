class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        min = -2**31
        max = 2**31 - 1
        
        if x == 0:
            return 0
        
        elif x > 0: 
            reverse = int(str(x)[::-1])
        
        elif x < 0:
            reverse = int(str(abs(x))[::-1]) * -1
        
        if reverse > min and reverse < max:
            return reverse
        else: 
            return 0
